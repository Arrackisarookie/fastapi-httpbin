from fastapi import APIRouter

redirect_router = APIRouter()


@redirect_router.get("/absolute-redirect/{n}", summary="Absolutely 302 Redirects n times.")
def get_absolute_redirect_n_times(n: int):
    return f"absolute redirect {n} times"


@redirect_router.delete("/redirect-to", summary="302/3XX Redirects to the given URL.")
def delete_redirect_to():
    return f"delete redirect to"


@redirect_router.get("/redirect-to", summary="302/3XX Redirects to the given URL.")
def get_redirect_to():
    return f"get redirect to"


@redirect_router.patch("/redirect-to", summary="302/3XX Redirects to the given URL.")
def patch_redirect_to():
    return f"patch redirect to"


@redirect_router.post("/redirect-to", summary="302/3XX Redirects to the given URL.")
def post_redirect_to():
    return f"post redirect to"


@redirect_router.put("/redirect-to", summary="302/3XX Redirects to the given URL.")
def put_redirect_to():
    return f"put redirect to"


@redirect_router.get("/redirect/{n}", summary="302 Redirects n times.")
def get_redirect_n_times(n: str):
    return f"get redirect {n} times"


@redirect_router.get("/relative-redirect/{n}", summary="Relatively 302 Redirects n times.")
def get_relative_redirect_n_times(n: str):
    return f"get relative redirect {n} times"
