import time
from starlette.middleware.base import BaseHTTPMiddleware


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        start_time = time.time()
        response = await call_next(request)
        elapsed = round((time.time() - start_time) * 1000, 2)
        response.headers["X-Response-Time-Ms"] = str(elapsed)
        return response
