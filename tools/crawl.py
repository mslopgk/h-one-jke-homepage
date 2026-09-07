# -*- coding: utf-8 -*-
import re, os, sys, json, time, hashlib
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse, unquote
import requests
from bs4 import BeautifulSoup

BASE = "http://jketech.co.kr"
HOST = "jketech.co.kr"
OUT = "mirror"
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36"}
KEEP_Q = {"bo_table", "wr_id", "sca", "page", "bo_id"}
SKIP_RE = re.compile(r"(write|login|register|logout|password|delete|comment|scrap|memo|poll|good|nogood|new\.php|search\.php|qalist|rss|print|move|page_link|/adm/|javascript:|mailto:|tel:)", re.I)
MAX_PAGES = 800

session = requests.Session()
session.headers.update(UA)

def norm(url, referer):
    u = urljoin(referer, url.strip())
    u = u.split("#")[0]
    p = urlparse(u)
    if p.netloc and p.netloc.replace("www.", "") != HOST:
        return None
    q = parse_qs(p.query, keep_blank_values=False)
    q = {k: v[0] for k, v in q.items() if k in KEEP_Q}
    query = urlencode(sorted(q.items()))
    path = p.path or "/"
    return urlunparse(("http", HOST, path, "", query, ""))

def local_path(url):
    p = urlparse(url)
    path = unquote(p.path)
    if path.endswith("/"):
        path += "index.html"
    if p.query:
        q = parse_qs(p.query)
        parts = [f"{k}-{v[0]}" for k, v in sorted(q.items())]
        root, ext = os.path.splitext(path)
        path = root + "__" + "_".join(parts) + (ext or ".html")
    path = re.sub(r"[^\w\-./가-힣]", "_", path)
    return os.path.join(OUT, path.lstrip("/"))

pages = {}      # url -> {path, title, links, status, ctype}
assets = {}     # url -> {path, size, ctype, referers}
queue = [BASE + "/", BASE + "/index.php", BASE + "/eng/index.php"]
seen = set(queue)

def save(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(content)

def fetch(url):
    for i in range(3):
        try:
            r = session.get(url, timeout=30)
            return r
        except Exception as e:
            time.sleep(1)
    return None

CSS_URL = re.compile(r"url\(\s*['\"]?([^'\")]+)['\"]?\s*\)")

def handle_css(url, text):
    found = []
    for m in CSS_URL.finditer(text):
        a = m.group(1)
        if a.startswith("data:"):
            continue
        n = norm(a, url)
        if n:
            found.append(n)
    for m in re.finditer(r"@import\s+(?:url\()?['\"]?([^'\")\s;]+)", text):
        n = norm(m.group(1), url)
        if n:
            found.append(n)
    return found

def is_page(ctype, url):
    return "text/html" in ctype

n = 0
asset_queue = []
while queue and n < MAX_PAGES:
    url = queue.pop(0)
    r = fetch(url)
    if r is None:
        pages[url] = {"status": "ERR"}
        continue
    ctype = r.headers.get("Content-Type", "")
    final = norm(r.url, url) or url
    if not is_page(ctype, url):
        asset_queue.append(url)
        continue
    n += 1
    r.encoding = r.apparent_encoding if "charset" not in ctype else r.encoding
    html = r.text
    lp = local_path(url)
    save(lp, r.content)
    soup = BeautifulSoup(html, "html.parser")
    title = soup.title.get_text(strip=True) if soup.title else ""
    links, imgs = [], []
    for tag in soup.find_all(["a", "area"]):
        h = tag.get("href")
        if not h or SKIP_RE.search(h):
            continue
        nu = norm(h, url)
        if nu and nu not in seen:
            seen.add(nu); queue.append(nu)
        if nu: links.append(nu)
    for tag in soup.find_all(["img", "script", "link", "source", "iframe", "embed", "video", "audio"]):
        for attr in ("src", "href", "data-src", "poster"):
            h = tag.get(attr)
            if not h or h.startswith("data:") or h.startswith("javascript"):
                continue
            if tag.name == "link" and tag.get("rel") and "stylesheet" not in tag.get("rel") and "icon" not in " ".join(tag.get("rel")):
                continue
            nu = norm(h, url)
            if nu:
                imgs.append(nu)
                assets.setdefault(nu, {"referers": set()})["referers"].add(url)
    # inline style url()
    for m in CSS_URL.finditer(html):
        a = m.group(1)
        if a.startswith("data:"): continue
        nu = norm(a, url)
        if nu:
            imgs.append(nu)
            assets.setdefault(nu, {"referers": set()})["referers"].add(url)
    pages[url] = {"path": lp, "title": title, "status": r.status_code, "final": final, "links": sorted(set(links)), "assets": sorted(set(imgs))}
    print(f"[{n}] {r.status_code} {url} -> {title}", flush=True)
    time.sleep(0.15)

for u in asset_queue:
    assets.setdefault(u, {"referers": set()})

# fetch assets, recursing into CSS
done = set()
aq = list(assets.keys())
while aq:
    u = aq.pop(0)
    if u in done: continue
    done.add(u)
    r = fetch(u)
    if r is None or r.status_code != 200:
        assets[u].update({"status": r.status_code if r else "ERR"})
        continue
    ctype = r.headers.get("Content-Type", "")
    lp = local_path(u)
    save(lp, r.content)
    assets[u].update({"status": 200, "path": lp, "size": len(r.content), "ctype": ctype})
    if "css" in ctype or u.endswith(".css"):
        for nu in handle_css(u, r.content.decode("utf-8", "ignore")):
            assets.setdefault(nu, {"referers": set()})["referers"].add(u)
            if nu not in done: aq.append(nu)
    print(f"[A] {len(r.content):>8} {u}", flush=True)

for a in assets.values():
    a["referers"] = sorted(a["referers"])
json.dump({"pages": pages, "assets": assets}, open("crawl_manifest.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("PAGES", len(pages), "ASSETS", len(assets))
