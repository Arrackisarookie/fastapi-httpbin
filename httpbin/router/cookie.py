from fastapi import APIRouter

cookie_router = APIRouter()


@cookie_router.get("/cookies")
def cookies():
    return "cookies"


@cookie_router.get("/cookies/delete")
def cookies_delete():
    return "cookies delete"


@cookie_router.get("/cookies/set")
def cookies_set():
    return "cookies set"


@cookie_router.get("/cookies/set/{name}/{value}")
def cookies(name: str, value: str):
    return f"cookies set {name} {value}"
