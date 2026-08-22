from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.schemas.auth import LoginResponse
from app.core.security import (
    verify_password,
    create_access_token
)


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


# Temporary test user
TEST_USERS = {
    "admin": {
        "password_hash": "$2b$12$XxQEZR91BNFZBSNGZ.WptuD3S.5tYAAMXXXVv4qgB9Nkp6VRrKcqS",
        "role": "system_admin"
    },
    "collegeadmin": {
        "password_hash": "$2b$12$IXwYlMK.xu7duH/jVpB.teMobf2f5uQ.h1ZRVB80mdiwwrtTqj3Um",
        "role": "college_admin"
    },
    "faculty": {
        "password_hash": "$2b$12$p4hiQTqNhWFz.kDqauO8ZOOQ8mYkfHJuXKZt2Kq0mtV09I5vODDm6",
        "role": "faculty"
    },
    "student": {
        "password_hash": "$2b$12$02FCUVwqFsCzkxyn.bn/6.ChuKwTwj7.ucqMaAIChSZP20mbtFCNO",
        "role": "student"
    }
}

@router.post("/login", response_model=LoginResponse)
def login(
    form_data: OAuth2PasswordRequestForm = Depends()
):
    user = TEST_USERS.get(form_data.username)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        form_data.password,
        user["password_hash"]
    ):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": form_data.username,
            "role": user["role"]
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }