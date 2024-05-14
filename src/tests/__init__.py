import pytest

from src.main import app_assembly

pytest_plugins = ('pytest_asyncio',)


@pytest.fixture
def app_http_client(loop, aiohttp_client):
    app = app_assembly()
    return loop.run_until_complete(aiohttp_client(app))