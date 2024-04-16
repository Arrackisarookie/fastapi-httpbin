from fastapi import APIRouter

response_inspection_router = APIRouter()


@response_inspection_router.get("/cache", summary="Returns a 304 if an If-Modified-Since header or If-None-Match is present. Returns the same as a GET otherwise.")
def get_cache():
    return f"cache"


@response_inspection_router.get("/cache/{value}", summary="Sets a Cache-Control header for n seconds.")
def get_cache_value(value: str):
    return f"cache {value}"


@response_inspection_router.get("/etag", summary="Assumes the resource has the given etag and responds to If-None-Match and If-Match headers appropriately.")
def get_etag():
    return f"etag"


@response_inspection_router.get("/response-headers", summary="Returns a set of response headers from the query string.")
def get_response_headers():
    return f"response headers"


@response_inspection_router.post("/response-headers", summary="Returns a set of response headers from the query string.")
def post_response_headers():
    return f"response headers"
