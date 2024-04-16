from fastapi import APIRouter

dynamic_data_router = APIRouter()


@dynamic_data_router.get("/base64/{value}", summary="Decodes base64url-encoded string.")
def get_base64_value(value: str):
    return f"get base64 value {value}"


@dynamic_data_router.get("/bytes/{n}", summary="Returns n random bytes generated with given seed")
def get_bytes_n(n: int):
    return f"get bytes n {n}"


@dynamic_data_router.delete("/delay/{delay}", summary="Returns a delayed response (max of 10 seconds).")
def delete_delay(delay: str):
    return f"delete delay {delay}"


@dynamic_data_router.get("/delay/{delay}", summary="Returns a delayed response (max of 10 seconds).")
def get_delay(delay: str):
    return f"get delay {delay}"


@dynamic_data_router.patch("/delay/{delay}", summary="Returns a delayed response (max of 10 seconds).")
def patch_delay(delay: str):
    return f"patch delay {delay}"


@dynamic_data_router.post("/delay/{delay}", summary="Returns a delayed response (max of 10 seconds).")
def post_delay(delay: str):
    return f"post delay {delay}"


@dynamic_data_router.put("/delay/{delay}", summary="Returns a delayed response (max of 10 seconds).")
def put_delay(delay: str):
    return f"put delay {delay}"


@dynamic_data_router.get("/drip", summary="Drips data over a duration after an optional initial delay.")
def get_drip():
    return f"get drip"


@dynamic_data_router.get("/links/{n}/{offset}", summary="Generate a page containing n links to other pages which do the same.")
def get_link_n_offset(n: int, offset: str):
    return f"get link {n} {offset}"


@dynamic_data_router.get("/range/{numbytes}", summary="Streams n random bytes generated with given seed, at given chunk size per packet.")
def get_range(numbytes: str):
    return f"get range {numbytes}"


@dynamic_data_router.get("/stream-bytes/{n}", summary="Streams n random bytes generated with given seed, at given chunk size per packet.")
def get_stream_bytes(n: int):
    return f"get stream bytes {n}"


@dynamic_data_router.get("/stream/{n}", summary="Stream n JSON responses")
def get_stream_n(n: str):
    return f"get stream {n}"


@dynamic_data_router.get("/uuid", summary="Return a UUID4.")
def get_uuid():
    return f"get uuid"
