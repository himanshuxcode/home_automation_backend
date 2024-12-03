from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    house_id: str

class UserLogin(BaseModel):
    username: str
    password: str
