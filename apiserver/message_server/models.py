from database import Base

from sqlalchemy import Column, Integer, String

class Message(Base):
    __tablename__='messages'
    id=Column(Integer, primary_key=True, index=True)
    account_id=Column(String)
    message_id=Column(Integer)
    sender_number=Column(String)
    receiver_number=Column(String)


