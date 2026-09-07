# -*- coding: utf-8 -*-
import re, json
from urllib.parse import urlparse, parse_qs, unquote
from playwright.sync_api import sync_playwright
def key(url):
    p = urlparse(url); q = parse_qs(p.query)
    path = p.path.strip("/").replace("/", "_").replace(".php","") or "index"
    if q: path += "__" + "_".join(f"{k}-{unquote(v[0])}" for k,v in sorted(q.items()))
    return re.sub(r"[^\w\-가-힣.]", "_", path)
retry = ["http://jketech.co.kr/bbs/board.php?bo_table=ceri1&page=4","http://jketech.co.kr/bbs/board.php?bo_table=ceri1&page=5",
 "http://jketech.co.kr/bbs/board.php?bo_table=ceri1&page=2&sca=%EB%9D%BC%EC%9D%B4%EC%84%BC%EC%8A%A4",
 "http://jketech.co.kr/bbs/board.php?bo_table=ceri1_en&page=2&sca=License",
 "http://jketech.co.kr/bbs/board.php?bo_table=sub03_01&sca=Normal+SWBD&wr_id=1",
 "http://jketech.co.kr/bbs/board.php?bo_table=sub03_06&sca=Normal+SWBD&wr_id=1"]
with sync_playwright() as pw:
    br = pw.chromium.launch(channel="chrome", headless=True)
    ctx = br.new_context(viewport={"width":1400,"height":900})
    page = ctx.new_page()
    for u in retry:
        k=key(u)
        try:
            page.goto(u, wait_until="load", timeout=60000); page.wait_for_timeout(1800)
            page.screenshot(path=f"screenshots/{k}.png", full_page=True); print("OK",k,flush=True)
        except Exception as e: print("FAIL",k,str(e)[:80],flush=True)
    for u, name in [("http://jketech.co.kr/", "index__gnb-hover"), ("http://jketech.co.kr/eng/index.php", "eng_index__gnb-hover")]:
        try:
            page.goto(u, wait_until="load", timeout=60000); page.wait_for_timeout(2500)
            page.hover(".gnb .depth1 >> nth=0"); page.wait_for_timeout(900)
            page.screenshot(path=f"screenshots/{name}.png"); print("OK",name,flush=True)
            if "eng" not in u:
                for i in range(1,4):
                    page.mouse.move(700,600)
                    page.click(f"#spaceSlideNav a >> nth={i}"); page.wait_for_timeout(2600)
                    page.screenshot(path=f"screenshots/index__slide{i+1}.png"); print("OK slide",i+1,flush=True)
                # footer quick-box hover
                page.hover(".foot_box >> nth=0"); page.wait_for_timeout(700)
                page.screenshot(path="screenshots/index__footbox-hover.png"); print("OK footbox",flush=True)
        except Exception as e: print("FAIL",name,str(e)[:120],flush=True)
    br.close()
