from fastapi import APIRouter ,Depends ,HTTPException
from Routers.auth import check_token
from sqlalchemy.orm import Session
from Databases.User import get_db
from Models.User import Task
from Models.User import User
from schemas.task import TaskRequest , TaskResponse
from datetime import datetime , timedelta 



router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"]
    )


@router.get("/upcoming", response_model=list[TaskResponse])
def get_overdue_tasks(db : Session = Depends(get_db) , email : str = Depends(check_token)):
    user = db.query(User).filter( User.email == email).first()

    if not user:
        raise HTTPException(status_code=404 , detail="انت مش مسجل حاول مجددا")

    tasks = db.query(Task).filter(Task.owner_id == user.id , Task.Due_Date > datetime.utcnow()).all() 
    if not tasks :
        raise HTTPException(status_code=404 , detail="مفيش أي مهمه موجود  , شكلك ماشي بالبركه")
    return tasks



@router.get("/overdue", response_model=list[TaskResponse])
def get_overdue_tasks(db : Session = Depends(get_db) , email : str = Depends(check_token)):
    user = db.query(User).filter( User.email == email).first()

    if not user:
        raise HTTPException(status_code=404 , detail="انت مش مسجل حاول مجددا")

    tasks = db.query(Task).filter(Task.owner_id == user.id , Task.Due_Date < datetime.utcnow()).all() 
    if not tasks :
        raise HTTPException(status_code=404 , detail="مفيش حاجه متراكمه عليك يا بطل")
    return tasks



@router.get("/" , response_model=list[TaskResponse])
def display_tasks(email : str = Depends(check_token) , db : Session = Depends(get_db)):
    user = db.query(User).filter( User.email == email).first()

    if not user:
        raise HTTPException(status_code=404 , detail="user not found")

    tasks = db.query(Task).filter(Task.owner_id == user.id).all()
    
    return tasks 

@router.post("/create")
def create_task( task : TaskRequest ,email : str = Depends(check_token) , db : Session = Depends(get_db)):
    user = db.query(User).filter( User.email == email).first()
    if not user:
        raise HTTPException(status_code=404 , detail="user not found")

    new_task = Task(
        Title = task.title ,
        TaskDescription = task.description ,
        Due_Date = task.due_date ,
        owner_id = user.id ,
    )
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return {"تم أضافه المهمه" : task}
    


@router.put("/update/{taskname}")
def update_task (taskname : str , task_update : TaskRequest , email : str = Depends(check_token) , db : Session = Depends(get_db)) :
    check_task  = db.query(Task).filter(taskname == Task.Title).first()
    if not check_task:
        raise HTTPException(status_code=404 , detail="المهمه غير موجوده")

    update_data = task_update.dict(exclude_unset=True)
    for field, value in update_data.items() :
        setattr(check_task , field , value)
    
    db.commit()
    db.refresh(check_task)
    return check_task


@router.delete("/delete/{Task.Title}")
def delete_task(taskname : str , email : str = Depends(check_token) , db : Session = Depends(get_db)):
    
    check_task  = db.query(Task).filter(taskname == Task.Title).first()
    if not check_task:
        raise HTTPException(status_code=404 , detail="المهمه غير موجوده")
    
    db.delete(check_task)
    db.commit()
    return {"message" : "تم حذف المهمه بنجاح"}



