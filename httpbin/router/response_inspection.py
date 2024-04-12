from fastapi import APIRouter

response_inspection_router = APIRouter()


@response_inspection_router.get("/cache")
def get_cache():
    return f"cache"


@response_inspection_router.get("/cache/{value}")
def get_cache_value(value: str):
    return f"cache {value}"


@response_inspection_router.get("/etag")
def get_etag():
    return f"etag"


@response_inspection_router.get("/response-headers")
def get_response_headers():
    return f"response headers"


@response_inspection_router.post("/response-headers")
def post_response_headers():
    return f"response headers"
