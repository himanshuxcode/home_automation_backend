from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from app.schemas.user import UserCreate, UserLogin
from app.crud.user import create_user, get_user_by_username
from app.core.security import create_access_token, get_password_hash, verify_password
from app.models.user import User
from app.core.config import settings

router = APIRouter()

@router.post("/signup", response_model=dict)
async def signup(user: UserCreate):
    user_in_db = await get_user_by_username(user.username)
    if user_in_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    
    user.hashed_password = get_password_hash(user.password)
    await create_user(User(**user.dict()))
    return {"msg": "User created successfully"}

@router.post("/login", response_model=dict)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await get_user_by_username(form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Invalid username or password")
    if not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(status_code=400, detail="Invalid username or password")
    
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user['username']}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type": "bearer"}
