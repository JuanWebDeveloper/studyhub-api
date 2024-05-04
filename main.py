from fastapi import FastAPI
from pymongo import MongoClient, errors
from pymongo import errors

api_app = FastAPI();
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