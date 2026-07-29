import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models import User

load_dotenv()

secret_key = os.environ.get("SECRET_KEY", "mysecretkey")
algorithm = os.environ.get("ALGORITHM", "HS256")
acess_token_expire_minutes = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login/")


def get_password_hash(password: str) -> str:
    # bcrypt is preferred over MD5 or SHA-256 for passwords because it is slow by design,
    # making brute-force attacks much more expensive and adding a salt automatically.
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=acess_token_expire_minutes)
    to_encode["exp"] = expire
    return jwt.encode(to_encode, secret_key, algorithm=algorithm)


async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)) -> User:
    credentials_error = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"error": {"code": "UNAUTHORIZED", "message": "Could not validate credentials", "field": None}},
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = jwt.decode(token, secret_key, algorithms=[algorithm])
        email = payload.get("sub")
        if email is None:
            raise credentials_error
    except JWTError:
        raise credentials_error

    result = await db.execute(select(User).where(User.email == email))
    user = result.scalar_one_or_none()
    if user is None:
        raise credentials_error

    return user
