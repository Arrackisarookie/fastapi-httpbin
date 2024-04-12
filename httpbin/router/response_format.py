from fastapi import APIRouter

response_format_router = APIRouter()


@response_format_router.get("/brotli")
def brotli():
    return "brotli"


@response_format_router.get("/deflate")
def deflate():
    return "deflate"


@response_format_router.get("/deny")
def deny():
    return "deny"


@response_format_router.get("/encoding/utf8")
def encoding_utf8():
    return "encoding utf8"


@response_format_router.get("/gzip")
def gzip():
    return "gzip"


@response_format_router.get("/html")
def html():
    return "html"


@response_format_router.get("/json")
def json():
    return "json"


@response_format_router.get("/robot.txt")
def robot():
    return "robot"


@response_format_router.get("/xml")
def xml():
    return "xml"
