from pydantic import BaseModel 
from typing import Optional
from datetime import datetime 
class TaskRequest(BaseModel):
    title : str 
    description : str  
    due_date : Optional[datetime] = None 

class TaskResponse(BaseModel):
    Title : str 
    TaskDescription : str 
    Is_Complete : Optional[bool] = False
    Due_Date : Optional[datetime] = None 

