from fastapi import APIRouter

anything_router = APIRouter()


@anything_router.delete("/anything", summary="Returns anything passed in request data.")
def delete_anything():
    return f"delete anything"


@anything_router.get("/anything", summary="Returns anything passed in request data.")
def get_anything():
    return f"get anything"


@anything_router.patch("/anything", summary="Returns anything passed in request data.")
def patch_anything():
    return f"patch anything"


@anything_router.post("/anything", summary="Returns anything passed in request data.")
def post_anything():
    return f"post anything"


@anything_router.put("/anything", summary="Returns anything passed in request data.")
def put_anything():
    return f"put anything"


@anything_router.delete("/anything/{anything}", summary="Returns anything passed in request data.")
def delete_anything(anything: str):
    return f"delete anything {anything}"


@anything_router.get("/anything/{anything}", summary="Returns anything passed in request data.")
def get_anything(anything: str):
    return f"get anything {anything}"


@anything_router.patch("/anything/{anything}", summary="Returns anything passed in request data.")
def patch_anything(anything: str):
    return f"patch anything {anything}"


@anything_router.post("/anything/{anything}", summary="Returns anything passed in request data.")
def post_anything(anything: str):
    return f"post anything {anything}"


@anything_router.put("/anything/{anything}", summary="Returns anything passed in request data.")
def put_anything(anything: str):
    return f"put anything {anything}"
