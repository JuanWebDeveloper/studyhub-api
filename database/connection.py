from motor.motor_asyncio import AsyncIOMotorClient

# Connection and creation of the database
mongo_client = AsyncIOMotorClient('mongodb://localhost:27017/')
studyhub_database = mongo_client.studyhub_storage