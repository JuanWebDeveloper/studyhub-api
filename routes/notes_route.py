from fastapi import APIRouter, HTTPException
from bson import ObjectId
from controllers.notes_controller import create_notes, get_all_notes, get_note_by_id, update_note, delete_note
from schemas.notes_schema import Note
from schemas.update_notes_schema import UpdateNote

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

# Define a GET route '/note/{note_id}' to retrieve a note by its ID from the database.
@notes_router.get("/note/{note_id}", response_model=Note)
async def fetch_note_by_id(note_id: str):
  note = await get_note_by_id(note_id)
  
  if note:
    return note
  raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found in the database. Please verify the ID and try again.")

# Define a PUT route '/update-note/{note_id}' to update a note in the database.
@notes_router.put("/update-note/{note_id}", response_model=Note)
async def update_note_by_id(note_id: str, updated_note: UpdateNote):
  updated_note_dict = updated_note.model_dump()
  response = await update_note(note_id, updated_note_dict)
  
  if response:
    return response
  raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found in the database. Please verify the ID and try again.")

# Define a DELETE route '/delete-note/{note_id}' to delete a note from the database.
@notes_router.delete("/delete-note/{note_id}")
async def remove_note_by_id(note_id: str):
  deletion_result = await delete_note(note_id)
  
  if deletion_result:
    return {"message": "Note deleted successfully."}
  raise HTTPException(status_code=404, detail=f"Note with ID {note_id} not found in the database. Please verify the ID and try again.")
