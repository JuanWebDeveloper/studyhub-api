from typing import Optional
from pydantic import BaseModel, Field

class UpdateNotes(BaseModel):
    title: Optional[str] = Field(None)
    content: Optional[str] = Field(None)
    category: Optional[bool] = Field(None)
	
