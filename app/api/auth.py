from functools import wraps

from fastapi import Request
from fastapi.responses import JSONResponse

from app.config import settings


def token_required(f):

    @wraps(f)
    async def decorator(*args, **kwargs):

        request: Request = kwargs.get("request") or next(
            (a for a in args if isinstance(a, Request)),
            None
        )

        if not request:
            return JSONResponse(
                {
                    "success": False,
                    "message": "Request object missing!"
                },
                status_code=500
            )

        token = request.headers.get("Authorization")

        if not token:
            return JSONResponse(
                {
                    "success": False,
                    "message": "Token is missing!"
                },
                status_code=403
            )

        try:
            # Expected format:
            # Authorization: Bearer your_token

            token = token.replace("Bearer ", "")

            if token != settings.API_TOKEN:
                return JSONResponse(
                    {
                        "success": False,
                        "message": "Token is invalid!"
                    },
                    status_code=403
                )

        except Exception:
            return JSONResponse(
                {
                    "success": False,
                    "message": "Token is invalid!"
                },
                status_code=403
            )

        return await f(*args, **kwargs)

    return decorator