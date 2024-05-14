from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from database.connection import studyhub_database
from schemas.notes_schema import Note
    
# Collection for the notes.
notes_collection = studyhub_database.notes

# Creates a new note in the database, retrieves it, and returns the created note.
async def create_notes(note_to_create: Note):
  note_to_create.id = str(ObjectId())
  encoded_note = jsonable_encoder(note_to_create)
  insertion_result = await notes_collection.insert_one(encoded_note)
  retrieved_note = await notes_collection.find_one({"_id": insertion_result.inserted_id})
  return retrieved_note

# Retrieves all notes from the database and returns them.
async def get_all_notes():
  all_notes = []
  notes_cursor = notes_collection.find({})
  async for note_document in notes_cursor:
    all_notes.append(Note(**note_document))
  return all_notes

# Retrieves a note by its ID from the database and returns it.
async def get_note_by_id(note_id: str):
  note = await notes_collection.find_one({'_id': note_id})	
  return note

# Retrieves a note by its title from the database and returns it.
async def get_note_by_title(note_title: str):
  note = await notes_collection.find_one({'title': note_title})
  return note

# Updates a note in the database and returns the updated note.
async def update_note(note_id: str, note_data: dict):
  # Remove any keys with values of None.
  note_data = {key: value for key, value in note_data.items() if value is not None}

  await notes_collection.update_one({'_id': note_id}, {'$set': note_data})
  updated_note = await notes_collection.find_one({'_id': note_id})
  return updated_note

# Deletes a note from the database and returns True if the deletion was successful.
async def delete_note(note_id: str):
  deletion_result = await notes_collection.delete_one({'_id': note_id})
  return deletion_result.deleted_count > 0