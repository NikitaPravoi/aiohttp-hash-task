import pytest

from src.main import app_assembly

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def app_http_client(event_loop, aiohttp_client):
    app = app_assembly()
    return event_loop.run_until_complete(aiohttp_client(app))