import pytest

from . import app_http_client


@pytest.mark.asyncio
async def test_healthcheck(app_http_client):
    resp = await app_http_client.get('/')
    assert resp.status == 200
