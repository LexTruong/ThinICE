from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import data_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=["*"],
    allow_headers=["*"]
)

app.include_router(data_router, prefix="/api/data")