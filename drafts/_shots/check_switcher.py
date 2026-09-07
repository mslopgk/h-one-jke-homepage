import asyncio, pathlib
from playwright.async_api import async_playwright
root = pathlib.Path(__file__).resolve().parent.parent
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        first=True
        for f in sorted(root.glob('*/v*.html')):
            pg = await b.new_page(viewport={'width':1440,'height':900})
            errs=[]; pg.on('pageerror', lambda e: errs.append(str(e)))
            await pg.goto(f.as_uri(), wait_until='load'); await pg.wait_for_timeout(1200)
            n = await pg.evaluate("document.querySelectorAll('#hone-switcher a.hs-btn:not(.hs-home)').length")
            on = await pg.evaluate("(document.querySelector('#hone-switcher .hs-btn.on')||{}).textContent")
            if first:
                await pg.screenshot(path=str(root/'_shots'/'switcher_demo.png'), clip={'x':300,'y':780,'width':840,'height':120}); first=False
            print(f.parent.name, f.stem, 'links=',n, 'current=',on, 'errors=',errs[:2])
            await pg.close()
        await b.close()
asyncio.run(main())
