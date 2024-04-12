from fastapi import APIRouter

anything_router = APIRouter()


@anything_router.delete("/anything")
def delete_anything():
    return f"delete anything"


@anything_router.get("/anything")
def get_anything():
    return f"get anything"


@anything_router.patch("/anything")
def patch_anything():
    return f"patch anything"


@anything_router.post("/anything")
def post_anything():
    return f"post anything"


@anything_router.put("/anything")
def put_anything():
    return f"put anything"


@anything_router.delete("/anything/{anything}")
def delete_anything(anything: str):
    return f"delete anything {anything}"


@anything_router.get("/anything/{anything}")
def get_anything(anything: str):
    return f"get anything {anything}"


@anything_router.patch("/anything/{anything}")
def patch_anything(anything: str):
    return f"patch anything {anything}"


@anything_router.post("/anything/{anything}")
def post_anything(anything: str):
    return f"post anything {anything}"


@anything_router.put("/anything/{anything}")
def put_anything(anything: str):
    return f"put anything {anything}"
