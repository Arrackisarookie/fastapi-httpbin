from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("/basic-auth/{user}/{passwd}", summary="Prompts the user for authorization using HTTP Basic Auth.")
def basic_auth(user: str, passwd: str):
    return f"basic-auth {user} {passwd}"


@auth_router.get("/bearer", summary="Prompts the user for authorization using bearer authentication.")
def bearer():
    return "bearer"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}", summary="Prompts the user for authorization using Digest Auth.")
def digest_auth(qop: str, user: str, passwd: str):
    return f"digest-auth {qop} {user} {passwd}"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}", summary="Prompts the user for authorization using Digest Auth + Algorithm.")
def digest_auth_and_algorithm(qop: str, user: str, passwd: str, algorithm: str):
    return f"digest-auth {qop} {user} {passwd} {algorithm}"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}", summary="Prompts the user for authorization using Digest Auth + Algorithm.")
def digest_auth_and_algorithm_stale_after(qop: str, user: str, passwd: str, algorithm: str, stale_after: str):
    return f"digest-auth {qop} {user} {passwd} {algorithm} {stale_after}"


@auth_router.get("hidden-basic-auth/{user}/{passwd}", summary="Prompts the user for authorization using HTTP Basic Auth.")
def hidden_basic_auth(user: str, passwd: str):
    return f"hidden-basic-auth {user} {passwd}"
