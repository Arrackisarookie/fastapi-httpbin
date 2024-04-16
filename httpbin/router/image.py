from fastapi import APIRouter

image_router = APIRouter()


@image_router.get("/image", summary="Returns a simple image of the type suggest by the Accept header.")
def image():
    return "image"


@image_router.get("/image/jpeg", summary="Returns a simple JPEG image.")
def image_jpeg():
    return "image jpeg"


@image_router.get("/image/png", summary="Returns a simple PNG image.")
def image_png():
    return "image png"


@image_router.get("/image/svg", summary="Returns a simple SVG image.")
def image_svg():
    return "image svg"


@image_router.get("/image/webp", summary="Returns a simple WEBP image.")
def image_webp():
    return "image webp"
