from fastapi import FastAPI 
from Routers import auth , task , tools , chatbot
from Databases.base import Base 
from Databases.User import engine
from fastapi.middleware.cors import CORSMiddleware 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"] ,
    allow_credentials = True ,
    allow_methods = ["*"] ,
    allow_headers = ["*"] ,


)
Base.metadata.create_all(bind=engine)


app.include_router(auth.router)
app.include_router(task.router)
app.include_router(tools.router)
app.include_router(chatbot.router)



