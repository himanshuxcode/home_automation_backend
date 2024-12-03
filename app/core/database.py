from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

client = None

async def connect_to_mongo():
    global client
    client = AsyncIOMotorClient(settings.MONGO_URI)
    print("Connected to MongoDB")

async def close_mongo_connection():
    client.close()
    print("MongoDB connection closed")

def get_database():
    return client[settings.MONGO_DB]
