from typing import List
from pydantic import BaseSettings
from sqlalchemy.axt.declarative import declarative_base

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = "mysql+asyncmy://root:@localhost:3306/faculdade"
    DBBaseModel = declarative_base()
    
    JWT_SECRET: srt = 'w311PgVcqiBIXEGXa_IuPpRUIdIdlx8CXU0ImmWHB1c'
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7
    
    class Config:
        caseSensitive = True
        
settings: Settings = Settings()

"""
import secrets 
token: str = secrets.token_urlsafe(32)  
"""