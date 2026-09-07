import sys, os, asyncio, pathlib
from playwright.async_api import async_playwright
root = pathlib.Path(__file__).resolve().parent.parent
targets = sys.argv[1:]
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        for t in targets:
            skill, ver = t.split('/')
            path = root / skill / (ver + '.html')
            if not path.exists(): print('MISSING', t); continue
            pg = await b.new_page(viewport={'width':1440,'height':900})
            errs = []
            pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('console', lambda m: errs.append(m.text) if m.type=='error' else None)
            await pg.goto(path.as_uri(), wait_until='load')
            await pg.wait_for_timeout(2500)
            await pg.screenshot(path=str(root/'_shots'/f'{skill}__{ver}_top.png'))
            h = await pg.evaluate('document.documentElement.scrollHeight')
            for y in range(0, h, 700):
                await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(120)
            await pg.evaluate('window.scrollTo(0,0)'); await pg.wait_for_timeout(500)
            await pg.screenshot(path=str(root/'_shots'/f'{skill}__{ver}_full.png'), full_page=True)
            print(t, 'h=',h, 'errors=', len(errs), (errs[:3] if errs else ''))
            await pg.close()
        await b.close()
asyncio.run(main())
