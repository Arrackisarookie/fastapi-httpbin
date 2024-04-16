from fastapi import APIRouter

http_method_router = APIRouter()


@http_method_router.delete("/delete", summary="The request's DELETE parameters.")
def delete():
    return "delete"


@http_method_router.get("/get", summary="The request's query parameters.")
def get():
    return "get"


@http_method_router.patch("/patch", summary="The request's PATCH parameters.")
def patch():
    return "patch"


@http_method_router.post("/post", summary="The request's POST parameters.")
def post():
    return "post"


@http_method_router.put("/put", summary="The request's PUT parameters.")
def put():
    return "put"
