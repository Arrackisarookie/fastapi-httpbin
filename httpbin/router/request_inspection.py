from fastapi import APIRouter

request_inspection_router = APIRouter()


@request_inspection_router.get("/headers", summary="Return the incoming request's HTTP headers.")
def headers():
    return f"headers"


@request_inspection_router.get("/ip", summary="Returns the requester's IP Address.")
def ip():
    return f"ip"


@request_inspection_router.get("/user-agent", summary="Return the incoming requests's User-Agent header.")
def user_agent():
    return f"user agent"
