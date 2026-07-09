from pydantic import BaseModel 

class ToolRequest(BaseModel):
    Channal_Name : str 
    Channal_Description : str 
    Channal_Category : str 
    Channal_Url : str 

