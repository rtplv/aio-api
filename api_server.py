from aiohttp import web

from app import api_server_logger, main_loop
from app.controllers.example import ExampleController


async def init_app():
    """Initialize the application server."""
    app = web.Application()

    app.router.add_route('POST', '/test', ExampleController.test)

    return app


if __name__ == "__main__":
    app = main_loop.run_until_complete(init_app())
    web.run_app(app, port=5000, access_log=api_server_logger)
