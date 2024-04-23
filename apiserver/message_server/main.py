from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, HTTPException, Path
from starlette import status
from pydantic import BaseModel,Field

import models
from database import engine,SessionLocal
from models import Message

app=FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

# Create Pydantic Request
class MessageRequest(BaseModel):
    account_id: str=Field(min_length=3,max_length=10)
    message_id: int
    sender_number: str=Field(max_length=10,min_length=10)
    receiver_number: str=Field(max_length=10,min_length=10)

@app.get("/get/messages",status_code=status.HTTP_200_OK)
async def read_all_messages(db: db_dependency ):
    return db.query(Message).all()


@app.get("/get/messages/{account_id}",status_code=status.HTTP_200_OK)
async def read_message_account_id(db:db_dependency,account_id: int=Path(gt=0)):
    messages=db.query(Message).filter(Message.account_id==account_id).first()
    if messages is not None:
        return messages
    raise HTTPException(status_code=404,detail='account_id not found')

@app.post("/create",status_code=status.HTTP_201_CREATED)
async def create_message(db:db_dependency, message_request: MessageRequest):
    message=Message(**message_request.dict())
    db.add(message)
    db.commit()


@app.get("/search")
async def search(db:db_dependency,message_id: str=None,sender_number: str=None,receiver_number: str=None):
    filtered_messages=[]
    if message_id:
        message_ids = [int(x) for x in message_id.split(",")]
        for msg in message_ids:
            filtered_messages.append(db.query(Message).filter(Message.message_id==msg).first())
    if sender_number:
        sender_numbers=[int(x) for x in sender_number.split(",")]
        for number in sender_numbers:
            filtered_messages.append(db.query(Message).filter(Message.message_id == number).first())
    if receiver_number:
        receiver_numbers=[int(x) for x in receiver_number.split(",")]
        for number in receiver_numbers:
            filtered_messages.append(db.query(Message).filter(Message.message_id == number).first())
    return filtered_messages







