from fastapi import APIRouter , Depends , HTTPException 
from sqlalchemy.orm import Session 
from Models.User import Tool
from schemas.tools import ToolRequest
from Databases.User import get_db
from .auth import check_token_role_admin
router = APIRouter(
    prefix="/tools" ,
    tags=["Tools"]
)

@router.get("/search")
def search ( category : str , db :Session = Depends(get_db) ):
    tools = db.query(Tool).filter(Tool.Category.ilike("%category%")).all()

    return tools 


@router.get("/")
def tools(db : Session = Depends(get_db)):
    tools = db.query(Tool).all()

    return tools


@router.post("/create_tool")
def create_tool(tool : ToolRequest , db : Session = Depends(get_db) , check = Depends(check_token_role_admin) ):
    is_tool = db.query(Tool).filter(Tool.Channal_Name == tool.Channal_Name).first()

    if is_tool : 
        raise HTTPException(status_code=401 , detail="هذه الاداه موجوده بالفعل")
    
    new_tool =Tool(
        Channal_Name = tool.Channal_Name ,
        Channal_Description = tool.Channal_Description ,
        Category = tool.Channal_Category ,
        Channal_Url = tool.Channal_Url
    )
    db.add(new_tool)
    db.commit()
    db.refresh(new_tool)
    
    return {"message : " : "تم أضافة الادأة"}



@router.put("/update_tool")
def update_tool (name_tool : str , tool : ToolRequest , db : Session = Depends(get_db) ,check = Depends(check_token_role_admin) ):
    is_tool = db.query(Tool).filter(Tool.Channal_Name == name_tool).first()

    if not is_tool : 
        raise HTTPException(status_code=401 , detail="هذه الاداه غير موجوده ")
    
    update_data = tool.dict(exclude_unset=True)
    for field, value in update_data.items() :
        setattr(is_tool , field , value)

    db.commit()
    db.refresh(is_tool)
    
    return {"message : " : "تم أضافة التغيرات"}



@router.delete("/delete_tool")
def delete_tool(name_tool : str  , db : Session = Depends(get_db) , check = Depends(check_token_role_admin) ):
    is_tool = db.query(Tool).filter(Tool.Channal_Name == name_tool).first()

    if not is_tool : 
        raise HTTPException(status_code=401 , detail="هذه الاداه غير موجوده ")
    
    db.delete(is_tool)
    db.commit()
    
    return {"message : " : "تم حذف التغيرات"}


