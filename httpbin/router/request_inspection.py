from fastapi import APIRouter

request_inspection_router = APIRouter()


@request_inspection_router.get("/headers")
def headers():
    return f"headers"


@request_inspection_router.get("/ip")
def ip():
    return f"ip"


@request_inspection_router.get("/user-agent")
def user_agent():
    return f"user agent"
