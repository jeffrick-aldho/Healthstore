from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.exceptions.custom_exceptions import NotFoundException


def register_exception_handlers(app: FastAPI):
    @app.exception_handler(NotFoundException)
    async def not_found_handler(_: Request, exc: NotFoundException):
        return JSONResponse(status_code=404, content={"detail": exc.message})
