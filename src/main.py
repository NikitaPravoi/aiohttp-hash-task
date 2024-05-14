import click
from aiohttp import web
from src.controllers import (healthcheck,
                         hash_string)


def app_assembly() -> web.Application:
    app = web.Application()

    app.add_routes([web.get('/', healthcheck),
                    web.post('/hash', hash_string),
                    ])
    return app


@click.command()
@click.option('--host', default='0.0.0.0')
@click.option('--port', default=8080)
def main(host: str, port: int):
    web.run_app(app_assembly(), host=host, port=port)


if __name__ == '__main__':
    main()
