from fastapi import APIRouter

image_router = APIRouter()


@image_router.get("/image")
def image():
    return "image"


@image_router.get("/image/jpeg")
def image_jpeg():
    return "image jpeg"


@image_router.get("/image/png")
def image_png():
    return "image png"


@image_router.get("/image/svg")
def image_svg():
    return "image svg"


@image_router.get("/image/webp")
def image_webp():
    return "image webp"
