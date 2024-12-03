from fastapi import FastAPI
from app.routers import auth
from app.core.config import settings
from app.core.database import connect_to_mongo, close_mongo_connection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, world!"}

# @app.on_event("startup")
# async def startup_db_client():
#     await connect_to_mongo()

# @app.on_event("shutdown")
# async def shutdown_db_client():
#     await close_mongo_connection()

# app.include_router(auth.router, prefix="/auth", tags=["auth"])
