from playwright.sync_api import sync_playwright
with sync_playwright() as pw:
    br = pw.chromium.launch(channel="chrome", headless=True)
    page = br.new_context(viewport={"width":1400,"height":900}, user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36").new_page()
    for u, name in [("http://jketech.co.kr/", "index"), ("http://jketech.co.kr/eng/index.php", "eng_index")]:
        page.goto(u, wait_until="load", timeout=60000); page.wait_for_timeout(2500)
        print(page.evaluate("document.querySelectorAll('.gnb .depth1').length"), page.evaluate("JSON.stringify(document.querySelector('.gnb .depth1').getBoundingClientRect())"))
        page.mouse.move(430, 40); page.wait_for_timeout(1000)
        page.screenshot(path=f"screenshots/{name}__gnb-hover.png"); print("OK", name)
        if name=="index":
            page.mouse.move(700,600); page.wait_for_timeout(300)
            for i in range(1,4):
                page.evaluate(f"document.querySelectorAll('#spaceSlideNav a')[{i}].click()"); page.wait_for_timeout(2800)
                page.screenshot(path=f"screenshots/index__slide{i+1}.png"); print("OK slide", i+1)
            page.mouse.move(200, 840); page.wait_for_timeout(800)
            page.screenshot(path="screenshots/index__footbox-hover.png"); print("OK footbox")
    br.close()
