from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



MONGO_URI = "mongodb+srv://me:Ns2Jd8zrfRB4JxxD@cluster0.lf78r.mongodb.net/fastapi?retryWrites=true&w=majority"

client = AsyncIOMotorClient(MONGO_URI)
db = client["fastapi_test"]
collection = db["test_test"]


class User(BaseModel):
    name: str
    email: str




@app.post('/adduser')
async def add_user(user:User):
   try:
     newUser = {"name": user.name, "email": user.email }
     result = await collection.insert_one(newUser)
     return JSONResponse(
      content={"message":"User added successfully", "id": str(result.inserted_id)},
      status_code=201
     )
   except Exception as e:
     return JSONResponse(content={"error": str(e)}, status_code=500)



@app.get('/getusers')
async def get_users():
  try:
    users = []
    res = await collection.find().to_list(length=1000)
    for user in res:
      user["_id"] = str(user["_id"])
      users.append(user)    
    return JSONResponse(content={"data": users}, status_code=200)



  except Exception as e:
    return JSONResponse(content={"error": str(e)}, status_code=500)
