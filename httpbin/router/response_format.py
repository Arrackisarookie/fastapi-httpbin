from fastapi import APIRouter

response_format_router = APIRouter()


@response_format_router.get("/brotli", summary="Returns Brotli-encoded data.")
def brotli():
    return "brotli"


@response_format_router.get("/deflate", summary="Returns Deflate-encoded data.")
def deflate():
    return "deflate"


@response_format_router.get("/deny", summary="Returns page denied by robots.txt rules.")
def deny():
    return "deny"


@response_format_router.get("/encoding/utf8", summary="Returns a UTF-8 encoded body.")
def encoding_utf8():
    return "encoding utf8"


@response_format_router.get("/gzip", summary="Returns GZip-encoded data.")
def gzip():
    return "gzip"


@response_format_router.get("/html", summary="Returns a simple HTML document.")
def html():
    return "html"


@response_format_router.get("/json", summary="Returns a simple JSON document.")
def json():
    return "json"


@response_format_router.get("/robot.txt", summary="Returns some robots.txt rules.")
def robot():
    return "robot"


@response_format_router.get("/xml", summary="Returns a simple XML document.")
def xml():
    return "xml"
