from passlib.context import CryptContext
import os

secret_key = os.environ.get("SECRET_KEY", "mysecretkey")
algorithm = os.environ.get("ALGORITHM", "HS256")
acess_token_expire_minutes = int(os.environ.get("ACCESS_TOKEN_EXPIRE_MINUTES", 30))
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_password_hash(password: str) -> str:
    # bcrypt is preferred over MD5 or SHA-256 for passwords because it is slow by design,
    # making brute-force attacks much more expensive and adding a salt automatically.
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)
