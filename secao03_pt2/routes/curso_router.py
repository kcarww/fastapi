from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/cursos")
async def getCursos():
    return [
        {"id": 1, "nome": "Python Fundamentos"},
    ]