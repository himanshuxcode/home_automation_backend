from pydantic import BaseModel, Field
from typing import Optional
from bson import ObjectId

class User(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id")
    username: str
    email: str
    hashed_password: str
    house_id: str
