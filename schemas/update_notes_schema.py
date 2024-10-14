from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field

class UpdateNote(BaseModel):
  title: Optional[str] = Field(None)
  content: Optional[str] = Field(None)
  category: Optional[str] = Field(None)
	
  class Config:
    arbitrary_types_allowed = True
    json_encoders = {
      ObjectId: str
    }