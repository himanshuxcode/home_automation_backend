from app.models.user import User
from app.core.database import get_database

async def get_user_by_username(username: str):
    db = get_database()
    return await db["users"].find_one({"username": username})

async def create_user(user: User):
    db = get_database()
    await db["users"].insert_one(user.dict(by_alias=True))
