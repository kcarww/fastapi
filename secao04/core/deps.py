from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession
from core.database import Session

async def getSession() -> Generator:
    session: AssyncSession = Session()
    
    try:
        yield session
    finally:
        await session.close()