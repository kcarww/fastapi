from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import Type

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+asyncmy://root:@localhost:3306/faculdade"
    DBBaseModel: Type = declarative_base()
    
    class Config:
        case_sensitive = True
        
settings = Settings()