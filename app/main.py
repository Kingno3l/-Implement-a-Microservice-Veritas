import logging
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import SessionLocal
from .models import User
from passlib.context import CryptContext
from jose import JWTError, jwt
from pydantic import BaseModel

# Setup logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = FastAPI()

# Constants
MAX_BCRYPT_BYTES = 72  # Maximum bcrypt password length
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Pydantic schemas
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

# Database dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Root endpoint
@app.get("/")
def read_root():
    return {"message": "Auth microservice is running"}

# Register endpoint
@app.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        if db_user:
            raise HTTPException(status_code=400, detail="Email already registered")

        # Truncate password to 72 bytes for bcrypt
        password_bytes = user.password.encode("utf-8")[:MAX_BCRYPT_BYTES]
        hashed_password = pwd_context.hash(password_bytes)

        new_user = User(username=user.username, email=user.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {"message": "User registered successfully"}
    except Exception as e:
        logger.exception("Error in register endpoint")
        raise HTTPException(status_code=500, detail=str(e))

# Login endpoint
@app.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):
    try:
        db_user = db.query(User).filter(User.email == user.email).first()
        password_bytes = user.password.encode("utf-8")[:MAX_BCRYPT_BYTES]
        if not db_user or not pwd_context.verify(password_bytes, db_user.password):
            raise HTTPException(status_code=400, detail="Invalid credentials")

        token_data = {"user_id": db_user.id}
        token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
        return {"access_token": token}
    except Exception as e:
        logger.exception("Error in login endpoint")
        raise HTTPException(status_code=500, detail=str(e))
