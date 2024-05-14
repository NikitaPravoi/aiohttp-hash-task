import hashlib
import pytest

from . import app_http_client


@pytest.mark.asyncio
async def test_hash_string_valid(app_http_client):
    response = await app_http_client.post('/hash', json={"string": "test"})
    assert response.status == 200
    json_response = await response.json()
    assert 'hash_string' in json_response
    assert json_response['hash_string'] == hashlib.sha256("test".encode()).hexdigest()


@pytest.mark.asyncio
async def test_hash_string_valid_empty_string(app_http_client):
    response = await app_http_client.post('/hash', json={"string": ""})
    assert response.status == 200
    json_response = await response.json()
    assert 'hash_string' in json_response
    assert json_response['hash_string'] == hashlib.sha256("".encode()).hexdigest()


@pytest.mark.asyncio
async def test_hash_string_invalid_field(app_http_client):
    response = await app_http_client.post('/hash', json={"invalid_field": "test"})
    assert response.status == 400
    json_response = await response.json()
    assert 'validation_errors' in json_response
    assert len(json_response['validation_errors']) > 0


@pytest.mark.asyncio
async def test_hash_string_invalid_type(app_http_client):
    response = await app_http_client.post('/hash', json={"string": 300})
    assert response.status == 400
    json_response = await response.json()
    assert 'validation_errors' in json_response
    assert len(json_response['validation_errors']) > 0


@pytest.mark.asyncio
async def test_hash_string_invalid_request_body(app_http_client):
    response = await app_http_client.post('/hash', json={})
    assert response.status == 400
    json_response = await response.json()
    assert 'validation_errors' in json_response
    assert len(json_response['validation_errors']) > 0
