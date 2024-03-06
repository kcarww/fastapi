from typing import Optional
from pydantic import BaseModel

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: str
    horas: int
    
cursos = [
    Curso(id=1, titulo="Python", aulas="10", horas=20),
    Curso(id=2, titulo="Java", aulas="20", horas=40),
]