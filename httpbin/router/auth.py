from fastapi import APIRouter

auth_router = APIRouter()


@auth_router.get("/basic-auth/{user}/{passwd}")
def basic_auth(user: str, passwd: str):
    return f"basic-auth {user} {passwd}"


@auth_router.get("/bearer")
def bearer():
    return "bearer"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}")
def digest_auth(qop: str, user: str, passwd: str):
    return f"digest-auth {qop} {user} {passwd}"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}")
def digest_auth_and_algorithm(qop: str, user: str, passwd: str, algorithm: str):
    return f"digest-auth {qop} {user} {passwd} {algorithm}"


@auth_router.get("/digest-auth/{qop}/{user}/{passwd}/{algorithm}/{stale_after}")
def digest_auth_and_algorithm_stale_after(qop: str, user: str, passwd: str, algorithm: str, stale_after: str):
    return f"digest-auth {qop} {user} {passwd} {algorithm} {stale_after}"


@auth_router.get("hidden-basic-auth/{user}/{passwd}")
def hidden_basic_auth(user: str, passwd: str):
    return f"hidden-basic-auth {user} {passwd}"
