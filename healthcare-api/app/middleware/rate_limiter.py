import time
from collections import defaultdict, deque

from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 120, per_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.per_seconds = per_seconds
        self.hits: dict[str, deque] = defaultdict(deque)

    async def dispatch(self, request, call_next):
        client_ip = request.client.host if request.client else "unknown"
        now = time.time()
        window = self.hits[client_ip]
        while window and window[0] < now - self.per_seconds:
            window.popleft()

        if len(window) >= self.max_requests:
            return JSONResponse(status_code=429, content={"detail": "Rate limit exceeded"})

        window.append(now)
        return await call_next(request)
