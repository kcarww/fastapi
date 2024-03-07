from fastapi import APIRouter
from api.v1.endpoints import curso

apiRouter = APIRouter()
apiRouter.include_router(curso.router, prefix='/cursos', tags=['cursos'])


