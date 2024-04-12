from fastapi import APIRouter

http_method_router = APIRouter()


@http_method_router.delete("/delete")
def delete():
    return "delete"


@http_method_router.get("/get")
def get():
    return "get"


@http_method_router.patch("/patch")
def patch():
    return "patch"


@http_method_router.post("/post")
def post():
    return "post"


@http_method_router.put("/put")
def put():
    return "put"
