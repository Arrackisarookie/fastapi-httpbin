from fastapi import APIRouter

status_code_router = APIRouter()


@status_code_router.delete("/delete/{status_code}", summary="Return status code or random status code if more than one are given")
def delete(status_code: int):
    return f"delete {status_code}"


@status_code_router.get("/get/{status_code}", summary="Return status code or random status code if more than one are given")
def get(status_code: int):
    return f"get {status_code}"


@status_code_router.patch("/patch/{status_code}", summary="Return status code or random status code if more than one are given")
def patch(status_code: int):
    return f"patch {status_code}"


@status_code_router.post("/post/{status_code}", summary="Return status code or random status code if more than one are given")
def post(status_code: int):
    return f"post {status_code}"


@status_code_router.put("/put/{status_code}", summary="Return status code or random status code if more than one are given")
def put(status_code: int):
    return f"put {status_code}"
