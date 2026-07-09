from sqlalchemy import Column , String , Integer ,Boolean , ForeignKey , DateTime 
from Databases.base import Base
from sqlalchemy.orm import relationship




class User(Base):
    __tablename__ = "users"
    id = Column(Integer , primary_key=True )
    email = Column(String)
    password = Column(String)
    role = Column(String , default="admin")
    tasks = relationship(
        "Task",
        back_populates="user"
    )
  
  
class Task (Base) :
    __tablename__ = "tasks"
    id = Column(Integer , primary_key=True )
    Title = Column(String )
    TaskDescription = Column(String)
    Is_Complete = Column(Boolean)
    Due_Date = Column( DateTime , nullable=True )
    owner_id = Column(Integer , ForeignKey("users.id"))
    user = relationship(
        "User",
        back_populates="tasks"
    )


class Tool(Base) :
    __tablename__ = "tools"
    id = Column(Integer , primary_key=True)
    Channal_Name = Column(String)
    Channal_Description = Column(String)
    Category = Column(String)
    Channal_Url = Column(String)
    