from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta
from typing import Optional
from fastapi.responses import JSONResponse

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# JWT Config
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# MongoDB Connection
MONGO_URI = "mongodb+srv://me:Ns2Jd8zrfRB4JxxD@cluster0.lf78r.mongodb.net/fastapi?retryWrites=true&w=majority"
client = AsyncIOMotorClient(MONGO_URI)
db = client["auth"]
collection = db["users"]
class User(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
# Password Hashing
def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hash_password):
    return pwd_context.verify(plain_password, hash_password)
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    print("JWT Token:", token)  # Debugging
    
    return token
@app.post("/register")
async def register(user: User):
    try:
        existing_user = await collection.find_one({"username": user.username})
        if existing_user:
            raise HTTPException(status_code=400, detail="User already registered")
        hashed_password = get_password_hash(user.password)
        await collection.insert_one({"username": user.username, "password": hashed_password})
        return {"message": "User registered successfully"}
    except Exception as e:
        return {"error": str(e)}
@app.post("/login")
async def login(user: User):
    db_user = await collection.find_one({"username": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        return JSONResponse(content={"error": "Invalid credentials"}, status_code=401)
    access_token = create_access_token({"sub": user.username}, timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    response_data = {"access_token": access_token, "token_type": "bearer"}
    return JSONResponse(content=response_data, status_code=200)

