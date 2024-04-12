from fastapi import APIRouter

redirect_router = APIRouter()


@redirect_router.get("/absolute-redirect/{n}")
def get_absolute_redirect_n_times(n: int):
    return f"absolute redirect {n} times"


@redirect_router.delete("/redirect-to")
def delete_redirect_to():
    return f"delete redirect to"


@redirect_router.get("/redirect-to")
def get_redirect_to():
    return f"get redirect to"


@redirect_router.patch("/redirect-to")
def patch_redirect_to():
    return f"patch redirect to"


@redirect_router.post("/redirect-to")
def post_redirect_to():
    return f"post redirect to"


@redirect_router.put("/redirect-to")
def put_redirect_to():
    return f"put redirect to"


@redirect_router.get("/redirect/{n}")
def get_redirect_n_times(n: str):
    return f"get redirect {n} times"


@redirect_router.get("/relative-redirect/{n}")
def get_relative_redirect_n_times(n: str):
    return f"get relative redirect {n} times"
