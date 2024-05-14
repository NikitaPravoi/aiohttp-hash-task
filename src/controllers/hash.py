from aiohttp import web
import hashlib
from .decorators import validate

hash_string_validator = {
    "string": (str, True, None)
}


@validate(hash_string_validator)
async def hash_string(request: web.Request) -> web.Response:
    return web.json_response({"hash_string": hashlib.sha256(request['validated_data']['string'].encode()).hexdigest()})
