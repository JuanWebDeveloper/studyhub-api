from fastapi import FastAPI
from pymongo import MongoClient, errors
from routes.notes_route import notes_router
from middlewares.cors_middleware import setup_cors

# Create a new FastAPI instance.
api_app = FastAPI();
# Create a new MongoClient instance to connect to the MongoDB database.
mc = MongoClient('mongodb://localhost:27017/')

@api_app.get("/connection-status")
def connection_status():
  try:
    # The 'ismaster' command is a lightweight operation used to check server availability.
    mc.admin.command('ismaster')
    return {
      "api_message": "Connection to the API is successful!",
      "db_connection": True,
      "db_message": "Connection to the database is successful!"
    }
  except errors.ConnectionFailure:
    return {
	  "api_message": "Connection to the API is successful!",
	  "db_connection": False,
	  "db_message": "Connection to the database failed!"
    }

# Incorporate the 'notes_router' into the main FastAPI application to handle note-related routes.
api_app.include_router(notes_router)

# Initialize CORS middleware settings.
setup_cors(api_app)