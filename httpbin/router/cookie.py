from fastapi import APIRouter

cookie_router = APIRouter()


@cookie_router.get("/cookies", summary="Returns cookie data.")
def cookies():
    return "cookies"


@cookie_router.get("/cookies/delete", summary="Deletes cookie(s) as provided by the query string and redirects to cookie list.")
def cookies_delete():
    return "cookies delete"


@cookie_router.get("/cookies/set", summary="Sets cookie(s) as provided by the query string and redirects to cookie list.")
def cookies_set():
    return "cookies set"


@cookie_router.get("/cookies/set/{name}/{value}", summary="Sets a cookie and redirects to cookie list.")
def cookies(name: str, value: str):
    return f"cookies set {name} {value}"
