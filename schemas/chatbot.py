from pydantic import BaseModel 

class TaskPlanRequest(BaseModel):
    task_name : str 
    available_hours_per_day : float 



class TaskPlanResponse(BaseModel):
    estimated_days : int 
    breakdown_type : str 
    plan : list[str]
    tips : list[str]

    