from fastapi import FastAPI
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from starlette.staticfiles import StaticFiles

from httpbin.meta import tags_metadata
from httpbin.router import (
    http_method_router,
    auth_router,
    status_code_router,
    request_inspection_router,
    response_inspection_router,
    response_format_router,
    dynamic_data_router,
    cookie_router,
    image_router,
    redirect_router,
    anything_router,
)

app = FastAPI(
    title="fastapi-httpbin",
    summary="A simple HTTP Request & Response Service implemented by FastAPI.",
    docs_url=None,
    redoc_url=None,
    openapi_tags=tags_metadata
)
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
        swagger_ui_parameters={"docExpansion": None, "defaultModelsExpandDepth": -1},
    )


@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()


@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="/status/redoc.standalone.js",
    )


app.include_router(http_method_router, tags=["HTTP Methods"])
app.include_router(auth_router, tags=["Auth"])
app.include_router(status_code_router, tags=["Status Codes"])
app.include_router(request_inspection_router, tags=["Request inspection"])
app.include_router(response_inspection_router, tags=["Response inspection"])
app.include_router(response_format_router, tags=["Response formats"])
app.include_router(dynamic_data_router, tags=["Dynamic data"])
app.include_router(cookie_router, tags=["Cookies"])
app.include_router(image_router, tags=["Images"])
app.include_router(redirect_router, tags=["Redirects"])
app.include_router(anything_router, tags=["Anything"])
