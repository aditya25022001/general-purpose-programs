from aiohttp import web

async def handle_post(request):
    reader = await request.multipart()
    while True:
        part = await reader.next()
        if part is None:
            break
        await part.read(decode=True)
    return web.Response(text="OK")

app = web.Application()
app.router.add_post('/', handle_post)

web.run_app(app, host='127.0.0.1', port=8080)
