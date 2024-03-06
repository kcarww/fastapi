from typing import Optional
from pydantic import BaseModel, validator

class Curso(BaseModel):
    id: Optional[int] = None
    titulo: str
    aulas: str
    horas: int
    
    @validator('titulo')
    def validarTitulo(cls, value):
        if len(value) < 3:
            raise ValueError('O título deve ter mais de 5 caracteres')
        return value
    
cursos = [
    Curso(id=1, titulo="Python", aulas="10", horas=20),
    Curso(id=2, titulo="Java", aulas="20", horas=40),
]