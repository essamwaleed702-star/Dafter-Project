from fastapi import APIRouter , Depends , HTTPException 
from schemas.chatbot import TaskPlanRequest , TaskPlanResponse 
from sqlalchemy.orm import Session 
from Services.al_service import generate_task_plan 
from Routers.auth import check_token
router = APIRouter(
    prefix="/AI_Chat",
    tags=["AI Chat"],
)

@router.post("/plan_task" , response_model= TaskPlanResponse)
def plan_task(request : TaskPlanRequest , check = Depends(check_token)):
    try:
        result = generate_task_plan(request.task_name, request.available_hours_per_day)
        return TaskPlanResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500 , detail=str(e))
        