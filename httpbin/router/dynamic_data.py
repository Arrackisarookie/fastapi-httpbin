from fastapi import APIRouter

dynamic_data_router = APIRouter()


@dynamic_data_router.get("/base64/{value}")
def get_base64_value(value: str):
    return f"get base64 value {value}"


@dynamic_data_router.get("/bytes/{n}")
def get_bytes_n(n: int):
    return f"get bytes n {n}"


@dynamic_data_router.delete("/delay/{delay}")
def delete_delay(delay: str):
    return f"delete delay {delay}"


@dynamic_data_router.get("/delay/{delay}")
def get_delay(delay: str):
    return f"get delay {delay}"


@dynamic_data_router.patch("/delay/{delay}")
def patch_delay(delay: str):
    return f"patch delay {delay}"


@dynamic_data_router.post("/delay/{delay}")
def post_delay(delay: str):
    return f"post delay {delay}"


@dynamic_data_router.put("/delay/{delay}")
def put_delay(delay: str):
    return f"put delay {delay}"


@dynamic_data_router.get("/drip")
def get_drip():
    return f"get drip"


@dynamic_data_router.get("/links/{n}/{offset}")
def get_link_n_offset(n: int, offset: str):
    return f"get link {n} {offset}"


@dynamic_data_router.get("/range/{numbytes}")
def get_range(numbytes: str):
    return f"get range {numbytes}"


@dynamic_data_router.get("/stream-bytes/{n}")
def get_stream_bytes(n: int):
    return f"get stream bytes {n}"


@dynamic_data_router.get("/stream/{n}")
def get_stream_n(n: str):
    return f"get stream {n}"


@dynamic_data_router.get("/uuid")
def get_uuid():
    return f"get uuid"
