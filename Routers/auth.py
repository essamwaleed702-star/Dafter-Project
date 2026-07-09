from fastapi import APIRouter , Depends , HTTPException ,status
from schemas.auth import Register , Login
from Databases.User import  get_db
from sqlalchemy.orm import Session
from Models.User import User
from passlib.context import CryptContext
import jwt
from datetime import datetime, timedelta 
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from core.config import get_settings 

router = APIRouter(
    prefix="/auth" ,
    tags=["Auth"]
)
Setting = get_settings()

SECRET_KEY = Setting.secret_key
ALGORITHEM = Setting.algorithm

pwd_context = CryptContext(schemes=["bcrypt"]  , deprecated = "auto")


@router.post("/register")
def register(register : Register  , db : Session = Depends(get_db)):
    check_email = db.query(User).filter(register.email == User.email).first()

    if check_email : 
        raise HTTPException(
            status_code=400 ,
            detail="This Email is Found"
        )

    hash_password = pwd_context.hash(register.password)

    new_register = User(
        email = register.email ,
        password = hash_password ,
    )
    db.add(new_register)
    db.commit()

    return {"message" :f"تم انشاء الحساب بنجاح "}


@router.post("/login")
def login(login : OAuth2PasswordRequestForm = Depends()  , db : Session = Depends(get_db)):
    check_email = db.query(User).filter(login.username == User.email).first()

    if not check_email : 
        raise HTTPException(
            status_code=400 ,
            detail="المستخدم غير موجود"
        ) 
    
    valied_password = pwd_context.verify(login.password ,check_email.password)
    if not valied_password  :
        raise HTTPException(
            status_code=401 ,
            detail= "كلمة المرور غير صحيحه"
        )

    # create token 

    expire =datetime.utcnow() + timedelta(minutes=35)

    payload = {
        "sub" : login.username ,
        "exp" : expire ,
        "role" : check_email.role
    }

    token = jwt.encode(payload , SECRET_KEY , algorithm=ALGORITHEM)
    
    return {"access_token" : token  , "token_type": "bearer"}
 


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def check_token (token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHEM])
        email = payload.get("sub")
        if email is None :
            raise HTTPException(status_code=401 , detail="توكن غير صالح")
        
    except jwt.PyJWKError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                            detail="التوكن منتهي الصلاحيه او غير صالح" ,
                            headers={"WWW-Authentication": "Bearer"})
    return email 


def check_token_role_admin (token : str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token , SECRET_KEY , algorithms=[ALGORITHEM])
        email = payload.get("sub")
        role = payload.get("role")
        if email is None :
            raise HTTPException(status_code=401 , detail="توكن غير صالح")
        if role != "admin":
            raise HTTPException(status_code=401 , detail="توكن غير صالح")
        
    except jwt.PyJWKError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED ,
                            detail="التوكن منتهي الصلاحيه او غير صالح" ,
                            headers={"WWW-Authentication": "Bearer"})
    
    return {"email" : email , "role" : role}

