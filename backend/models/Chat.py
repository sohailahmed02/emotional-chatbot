from pydantic import BaseModel
from typing import Optional, List
from .Message import MessageModel
from datetime import datetime


class ChatModel(BaseModel):
    ChatID : str
    messages : List[MessageModel]
    CreatedAt : datetime

