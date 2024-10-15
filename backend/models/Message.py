from pydantic import BaseModel
from typing import Optional, List
from .Content import ContentModel

class MessageModel(BaseModel):
    createdAt: str
    user : str
    content : List[ContentModel]
    type : str  
