from fastapi import APIRouter, HTTPException
from bson import ObjectId
from controllers.notes_controller import create_notes, get_all_notes
from schemas.notes_schema import Note


# Create a new APIRouter instance to handle note-related routes.
notes_router = APIRouter()

# Define a POST route '/create-note' to create a new note in the database.
@notes_router.post("/create-note")
async def save_notes(new_note: Note):	
  new_note_dict = new_note.model_dump()
  new_note_dict["_id"] = ObjectId()
  new_note_model = Note(**new_note_dict)
  response = await create_notes(new_note_model)
    
  if response:
    return response
  raise HTTPException(status_code=400, detail="Note creation failed. Please check the input data and try again.")

# Define a GET route '/all-notes' to retrieve all notes from the database.
@notes_router.get("/all-notes")
async def fetch_all_notes():
  all_notes = await get_all_notes()
  return all_notes