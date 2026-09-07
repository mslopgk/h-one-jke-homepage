import sys, asyncio, pathlib
from playwright.async_api import async_playwright
root = pathlib.Path(__file__).resolve().parent.parent
# args: skill/ver y1,y2,...
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(channel='chrome')
        for spec in sys.argv[1:]:
            t, ys = spec.split(':')
            skill, ver = t.split('/')
            pg = await b.new_page(viewport={'width':1440,'height':900})
            await pg.goto((root/skill/(ver+'.html')).as_uri(), wait_until='load')
            await pg.wait_for_timeout(1500)
            for y in ys.split(','):
                await pg.evaluate(f'window.scrollTo(0,{y})'); await pg.wait_for_timeout(900)
                await pg.screenshot(path=str(root/'_shots'/f'{skill}__{ver}_y{y}.png'))
            print(spec, 'ok'); await pg.close()
        await b.close()
asyncio.run(main())
