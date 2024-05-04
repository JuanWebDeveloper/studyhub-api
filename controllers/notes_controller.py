from bson import ObjectId
from fastapi.encoders import jsonable_encoder
from database.connection import studyhub_database
from schemas.notes_schema import Note

# Collection for the notes.
notes_collection = studyhub_database.notes

# Creates a new note in the database, retrieves it, and returns the created note.
async def create_note(note_to_create: Note):
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
