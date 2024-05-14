from aiohttp import web
from typing import Callable, Dict, Tuple, Type, Union, Any

# ValidationParameters: (instance, required, default)
type ValidationParameters = Tuple[Type, bool, Union[str, int, float, None]]

example = {
    "field": ValidationParameters
}


def validate(validation_dict: Dict[str, ValidationParameters]) -> Callable:
    def decorator(handler: Callable) -> Callable:
        async def wrapper(request: web.Request) -> web.Response:
            if request.method in ['POST', 'PUT', 'PATCH']:
                try:
                    request_body = await request.json()
                except Exception as e:
                    return web.json_response({'error': 'Invalid JSON'}, status=400)

                response_body = {"validation_errors": []}

                for field, params in validation_dict.items():
                    field_type, required, default_value = params

                    if field in request_body:
                        if not isinstance(request_body[field], field_type):
                            response_body["validation_errors"].append(
                                f"Field '{field}' must be of type {field_type.__name__}."
                            )
                    else:
                        if required:
                            response_body["validation_errors"].append(
                                f"Field '{field}' is required."
                            )
                        else:
                            request_body[field] = default_value

                if response_body["validation_errors"]:
                    return web.json_response(response_body, status=400)
            else:
                request_body = {}

            request["validated_data"] = request_body
            return await handler(request)

        return wrapper
    return decorator
