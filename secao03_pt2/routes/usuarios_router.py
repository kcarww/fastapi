from fastapi import APIRouter

router = APIRouter()

@router.get("/api/v1/usuarios")
async def getUsuarios():
    return [
        {"info": "Todos os users"},
    ]