# -*- coding: utf-8 -*-
import json, re, sys, asyncio
from urllib.parse import urlparse, parse_qs, unquote
from playwright.sync_api import sync_playwright

m = json.load(open("crawl_manifest.json", encoding="utf-8"))
urls = [u for u,p in m["pages"].items() if p.get("status")==200]
def key(url):
    p = urlparse(url); q = parse_qs(p.query)
    path = p.path.strip("/").replace("/", "_").replace(".php","") or "index"
    if q: path += "__" + "_".join(f"{k}-{unquote(v[0])}" for k,v in sorted(q.items()))
    return re.sub(r"[^\w\-가-힣.]", "_", path)
# dedupe: skip page=1 variants and /index.php (same as /)
urls = [u for u in urls if "page=1&" not in u and not u.endswith("page=1") and u != "http://jketech.co.kr/index.php"]
print(len(urls), "pages to shoot", flush=True)
with sync_playwright() as pw:
    br = pw.chromium.launch(channel="chrome", headless=True)
    ctx = br.new_context(viewport={"width":1400,"height":900}, device_scale_factor=1, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120 Safari/537.36")
    page = ctx.new_page()
    done = []
    for u in urls:
        k = key(u)
        try:
            page.goto(u, wait_until="load", timeout=45000)
            page.wait_for_timeout(1800)
            page.screenshot(path=f"screenshots/{k}.png", full_page=True)
            done.append((u, f"screenshots/{k}.png"))
            print("OK", k, flush=True)
        except Exception as e:
            print("FAIL", k, str(e)[:100], flush=True)
    # main page: GNB hover state (KR + EN)
    for u, name in [("http://jketech.co.kr/", "index__gnb-hover"), ("http://jketech.co.kr/eng/index.php", "eng_index__gnb-hover")]:
        try:
            page.goto(u, wait_until="load", timeout=45000); page.wait_for_timeout(2500)
            page.hover(".gnb .depth1 >> nth=0"); page.wait_for_timeout(900)
            page.screenshot(path=f"screenshots/{name}.png", full_page=False)
            print("OK", name, flush=True)
            # slides 2-4 by clicking pager dots
            if "eng" not in u:
                for i in range(1,4):
                    page.mouse.move(700,600)
                    page.click(f"#spaceSlideNav a >> nth={i}"); page.wait_for_timeout(2600)
                    page.screenshot(path=f"screenshots/index__slide{i+1}.png", full_page=False)
                    print("OK slide", i+1, flush=True)
        except Exception as e:
            print("FAIL", name, str(e)[:120], flush=True)
    br.close()
json.dump(done, open("screenshots/_index.json","w",encoding="utf-8"), ensure_ascii=False, indent=1)
