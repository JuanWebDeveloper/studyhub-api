from typing import Optional
from bson import ObjectId
from pydantic import BaseModel, Field
from utils.objectid_validator import PyObjectIdValidator

class Notes(BaseModel):
    id: PyObjectIdValidator = Field(default_factory=PyObjectIdValidator, alias='_id')
    title: str
    content: Optional[str] = Field(None)
    category: str
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }
    
	
