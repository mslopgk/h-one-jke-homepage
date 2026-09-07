# -*- coding: utf-8 -*-
import json, re, os
from bs4 import BeautifulSoup, Comment
from urllib.parse import unquote, urlparse, parse_qs

m = json.load(open("crawl_manifest.json", encoding="utf-8"))
P = m["pages"]

def decode(b):
    head = b[:2000].decode("latin-1", "ignore").lower()
    mm = re.search(r'charset=["\']?([\w-]+)', head)
    enc = mm.group(1) if mm else None
    for e in ([enc] if enc else []) + ["utf-8", "cp949"]:
        try:
            t = b.decode(e)
            if "�" in t: raise UnicodeDecodeError(e, b, 0, 1, "repl")
            return t, e
        except Exception:
            continue
    return b.decode("cp949", "ignore"), "cp949?"

def clean(soup):
    for t in soup(["script", "style", "noscript", "form"]):
        # keep forms for board lists (they wrap content) -> only unwrap
        if t.name == "form": t.unwrap()
        else: t.decompose()
    for c in soup.find_all(string=lambda s: isinstance(s, Comment)): c.extract()

def md_of(node, base):
    out = []
    def walk(n, depth=0):
        if isinstance(n, str):
            s = re.sub(r"\s+", " ", n)
            if s.strip(): out.append(s)
            return
        name = n.name
        if name in ("h1","h2","h3","h4"):
            out.append("\n\n" + "#"*(int(name[1])+1) + " " + n.get_text(" ", strip=True) + "\n\n"); return
        if name == "img":
            src = n.get("src",""); alt = n.get("alt","")
            out.append(f"\n![{alt}]({src})\n"); return
        if name == "a":
            href = n.get("href","")
            inner = n.get_text(" ", strip=True)
            imgs = n.find_all("img")
            if imgs:
                for i in imgs: walk(i)
            if inner: out.append(f"[{inner}]({href})")
            return
        if name == "br": out.append("\n"); return
        if name == "table":
            rows=[]
            for tr in n.find_all("tr"):
                cells=[re.sub(r"\s+"," ",c.get_text(" ",strip=True)).replace("|","/") for c in tr.find_all(["th","td"])]
                if any(cells): rows.append(cells)
            if rows:
                w=max(len(r) for r in rows)
                rows=[r+[""]*(w-len(r)) for r in rows]
                out.append("\n\n| "+" | ".join(rows[0])+" |\n|"+"---|"*w+"\n")
                for r in rows[1:]: out.append("| "+" | ".join(r)+" |\n")
                out.append("\n")
            return
        if name in ("p","div","li","tr","dt","dd","section","article","ul","ol","table","address","caption","nav"):
            out.append("\n")
            if name == "li": out.append("- ")
        if name in ("td","th"):
            out.append(" | ")
        for c in n.children: walk(c, depth+1)
        if name in ("p","div","li","tr","dt","dd","section","article","ul","ol","table","address","nav"):
            out.append("\n")
    walk(node)
    txt = "".join(out)
    txt = re.sub(r"[ \t]+\n", "\n", txt)
    txt = re.sub(r"\n{3,}", "\n\n", txt)
    txt = re.sub(r"(\n- \s*\n)+", "\n", txt)
    return txt.strip()

def page_key(url):
    p = urlparse(url); q = parse_qs(p.query)
    path = p.path.strip("/").replace("/", "_").replace(".php","") or "index"
    if q:
        path += "__" + "_".join(f"{k}-{unquote(v[0])}" for k,v in sorted(q.items()))
    return re.sub(r"[^\w\-가-힣.]", "_", path)

os.makedirs("content", exist_ok=True)
index = []
for url, p in sorted(P.items()):
    if p.get("status") != 200 or "path" not in p: continue
    b = open(p["path"], "rb").read()
    html, enc = decode(b)
    soup = BeautifulSoup(html, "html.parser")
    clean(soup)
    title = soup.title.get_text(strip=True) if soup.title else ""
    # main content region
    main = soup.select_one(".sub_layout") or soup.select_one("#container") or soup.body
    # breadcrumb / left menu
    visual = soup.select_one(".s_visual_t p")
    sitemap = soup.select_one(".sitemap")
    left = soup.select_one(".left_menu")
    leftitems = []
    if left:
        for li in left.find_all("li"):
            a = li.find("a")
            if a: leftitems.append(("*" if "on" in (li.get("class") or []) else "") + a.get_text(strip=True) + " -> " + a.get("href",""))
    crumb = sitemap.get_text(" ", strip=True) if sitemap else ""
    if sitemap: sitemap.decompose()
    body_md = md_of(main, url) if main else ""
    imgs = [i.get("src") for i in (main.find_all("img") if main else []) if i.get("src")]
    key = page_key(url)
    with open(f"content/{key}.md", "w", encoding="utf-8") as f:
        f.write(f"# {crumb or title or key}\n\n")
        f.write(f"- URL: {url}\n- 인코딩: {enc}\n- 섹션 비주얼 타이틀: {visual.get_text(strip=True) if visual else '-'}\n")
        if leftitems: f.write("- 좌측메뉴: " + " / ".join(leftitems) + "\n")
        f.write("\n## 본문\n\n" + body_md + "\n")
        if imgs: f.write("\n## 본문 이미지\n\n" + "\n".join(f"- {i}" for i in imgs) + "\n")
    index.append({"url": url, "file": f"content/{key}.md", "crumb": crumb, "visual": visual.get_text(strip=True) if visual else "", "enc": enc, "n_img": len(imgs), "n_chars": len(body_md)})
json.dump(index, open("content/_index.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
for i in index: print(f"{i['n_chars']:>6}c {i['n_img']:>3}img {i['enc']:<6} {i['url']} | {i['crumb'][:50]}")
