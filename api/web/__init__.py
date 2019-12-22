import time
# import logging

from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from starlette.requests import Request
from starlette.middleware.gzip import GZipMiddleware
from starlette.middleware.cors import CORSMiddleware

from api.web import endpoints


# _logger = logging.getLogger(__name__)

app = FastAPI()
app.add_middleware(GZipMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost",
        "http://localhost:3000",
        "http://localhost:9000",
        "https://find-here-pois-client.herokuapp.com"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(endpoints.router)


def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Find POI-s via HERE",
        version="0.0.1",
        description="A simple API for finding POI-s using the HERE Places API",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi  # type: ignore


# @app.on_event("startup")
# async def startup():
#     _logger.info("Starting")
#
#
# @app.on_event("shutdown")
# async def shutdown():
#     _logger.info("Shutting down")


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["x-process-time"] = f"{process_time:.3f}"
    return response

