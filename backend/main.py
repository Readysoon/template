from fastapi import FastAPI, Depends, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from surrealdb import Surreal
import logging

from app.db.dbController import router as db_router

app = FastAPI()

# Configure CORS to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

app.include_router(db_router)

@app.get("/")
async def read_root():
	return {"Hello": "World!"}




