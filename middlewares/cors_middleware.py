from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from decouple import config

# Configure CORS middleware for the FastAPI.
def setup_cors(api_app: FastAPI):
  origin = config('DEV_FRONTEND_URL')

  api_app.add_middleware(
    CORSMiddleware,
    allow_origins=origin,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
  )