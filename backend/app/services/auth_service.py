from app.core.security import (
    verify_password,
    hash_password,
    create_access_token
)


DEMO_USER = {
    "username": "admin",
    "password_hash": hash_password("admin123"),
    "role": "system_admin"
}


def authenticate_user(username: str, password: str):

    if username != DEMO_USER["username"]:
        return None

    if not verify_password(
        password,
        DEMO_USER["password_hash"]
    ):
        return None

    return DEMO_USER


def login_user(username: str, password: str):

    user = authenticate_user(username, password)

    if user is None:
        return None

    access_token = create_access_token(
        {
            "sub": user["username"],
            "role": user["role"]
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }