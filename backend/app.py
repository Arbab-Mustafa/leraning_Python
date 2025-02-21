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
db = client["fastapi"]
collection = db["test"]

class Item(BaseModel):
    name: str
    description: str

@app.post("/additem")
async def add_item(item: Item):
    try:
        new_item = {"name": item.name, "description": item.description}
        result = await collection.insert_one(new_item)
        return JSONResponse(content={"message": "Item added successfully", "id": str(result.inserted_id)}, status_code=201)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/getitems")
async def get_items():
    try:
        items = []
        res = await collection.find().to_list(length=1000)
        for item in res:
            item["_id"] = str(item["_id"])  # Convert ObjectId to string
            items.append(item)
        return JSONResponse(content={"data": items}, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
