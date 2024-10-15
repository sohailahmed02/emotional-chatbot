from fastapi import FastAPI, HTTPException
import uuid
from datetime import datetime
from typing import List

from models.Chat import ChatModel 
from database.dbConnection import client
from models.Message import MessageModel
from models.Content import ContentModel



app = FastAPI(
    title="Student Course API",
    summary="A sample application showing how to use FastAPI to add a ReST API to a MongoDB collection.",
)


db = client.chat

# Create a unique chat ID
chat_id = str(uuid.uuid4())
myemail ="sohailahmed02@hotmai  .com"

# @app.post("/addchat")
def AddChat(chat:ChatModel, emailID:str):
    if emailID not in db.list_collection_names():
        db.create_collection(emailID)      
    user_collection = db.get_collection(emailID)    
    result = user_collection.insert_one(chat.dict())
    if not result:
        raise HTTPException(status_code=400, detail="Failed to create new chat")
    return {"status": "Chat added", "chatId": chat.ChatID}

mychat = ChatModel(
    ChatID= str(uuid.uuid4()),
    messages = [],
    CreatedAt = str(datetime.now()))

AddChat(mychat,myemail)




@app.post("/addmessage")
def AddMessage(message:MessageModel,emailID:str,ChatID:str):
    user_collection = db.get_collection(emailID)  
    # print(user_collection)
    result = user_collection.find_one_and_update(
        {"ChatId": ChatID},
        {"$push": {"messages": message.dict()}})
    print("result",result)
    if not result:
        raise HTTPException(status_code=400, detail="Failed to add new message")
    return {"status": "message added"}

myemailid = "sohailahmed02@hotmail.com"
mychatid = "e0118df5-431f-4eba-af24-9f316a765f76"
myContent = ContentModel(
    value = """The dataset has been successfully saved as both a 
    CSV file and an Excel file. You can download the files using 
    the links below:\n\n- [Download cities_dataset.csv]
    (sandbox:/mnt/data/cities_dataset.csv)\n- 
    [Download cities_dataset.xlsx]
    (sandbox:/mnt/data/cities_dataset.xlsx)\n\nLet me know if
    there's anything else you'd like to do with this dataset!"""
)

mymessage = MessageModel(
    createdAt = str(datetime.now()),
    user = "user",
    content = [myContent],
    type = "text"  
)

# AddMessage(mymessage, myemailid,mychatid)


@app.get("/allchats")
def AllChats(emailID:str):
    user_collection = db.get_collection(emailID)  
    result = user_collection.find().sort("CreatedAt",)
    print("result", list(result))
    for chat in list(result):
        pass
        # print("result",chat["messages"])
    if not result:
        raise HTTPException(status_code=400, detail="Failed to get chats")
    return {"status": "get chats", "chats": list(result) }

# AllChats(myemailid)


@app.delete("/delchat")
def DelChat(emailID:str , ChatID:str):
    user_collection = db.get_collection(emailID)  
    result = user_collection.delete_one({"ChatId": ChatID})
    if not result:
        raise HTTPException(status_code=400, detail="Failed to delete chat")
    return {"status": "chat deleted successfully"}


# DelChat(myemailid,mychatid)