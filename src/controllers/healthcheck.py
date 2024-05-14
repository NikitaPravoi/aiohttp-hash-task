from aiohttp import web


async def healthcheck(request: web.Request):
    return web.json_response(body=None, status=200)
