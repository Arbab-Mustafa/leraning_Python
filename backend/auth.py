from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from motor.motor_asyncio import AsyncIOMotorClient
from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from typing import Optional
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
# OAuth2 scheme
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Password Hashing
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

@app.get("/")
async def get_users():
    try:
        users = await collection.find().to_list(length=1000)
        
        # Convert ObjectId to string
        for user in users:
            user["_id"] = str(user["_id"])

        return users

    except Exception as e:
        return {"error": str(e)}


async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        
        if username is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token: missing subject",
                headers={"WWW-Authenticate": "Bearer"},
            )

        user = await collection.find_one({"username": username})

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found",
            )

        return user

    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
def serialize_mongo_doc(doc):
    """Converts MongoDB document to a serializable format."""
    if doc:
        doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
    return doc
@app.get("/me")
async def read_users_me(user: dict = Depends(get_current_user)):
    return jsonable_encoder(serialize_mongo_doc(user))

         

    