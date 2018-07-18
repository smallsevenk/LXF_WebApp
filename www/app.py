import logging;logging.basicConfig(level=logging.INFO)

import asyncio
from aiohttp import web

async def index(request):
    return web.Response(body=b'<h1>welcome to my webapp</h1>', content_type='text/html')

async def init(lp):
    app = web.Application(loop=lp)
    app.router.add_route('GET', '/', index)
    srv = await lp.create_server(app.make_handler(), '127.0.0.1', 8000)
    logging.info('server started at http://127.0.0.1:8000')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

