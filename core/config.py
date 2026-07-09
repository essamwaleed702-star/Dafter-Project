from pydantic_settings import BaseSettings
from functools import lru_cache
class Setting(BaseSettings):
    GEMINI_API_KEY : str
    secret_key : str 
    algorithm : str


    class Config :
        env_file =".env"
    
@lru_cache
def get_settings():
    return Setting()
