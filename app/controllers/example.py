from aiohttp import web


class ExampleController:
    @staticmethod
    async def test(request):
        return web.json_response({'success': True})
