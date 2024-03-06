from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from models import Curso, cursos
from typing import Optional, List, Any
from fastapi.responses import JSONResponse, Response
from fastapi import Path, Query, Header, Depends
from time import sleep


app = FastAPI(title="Testando fastApi",
              description="Exemplo de testes",
              version="1.0.0")

def loading() -> None:
    try:
        print('Carregando...')
        
    finally:
        print('Fechando')



@app.get('/cursos',
         response_model=List[Curso],
         response_description="Lista de cursos")
async def getCursos():
    return cursos

@app.get('/cursos/{curso_id}')
async def getCursoById(curso_id: int):
    for curso in cursos:
        if curso.id == curso_id:
            return curso
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.post('/cursos', status_code=status.HTTP_201_CREATED, response_model=Curso)
async def createCurso(curso: Curso):
    next_id = len(cursos) + 1
    curso.id = next_id
    cursos.append(curso)
    return curso 
    # raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Curso já existe")


@app.put('/cursos/{curso_id}', status_code=status.HTTP_202_ACCEPTED)
async def updateCurso(curso_id: int, curso: Curso):
    if curso_id in cursos:
        cursos[curso_id] = curso
        return cursos[curso_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.delete('/cursos/{curso_id}', status_code=status.HTTP_204_NO_CONTENT)
async def deleteCurso(curso_id: int):
    if curso_id in cursos:
        del cursos[curso_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")

@app.get('/calculadora')
async def calculadora(a: int = Query(default=0), b: int = Query(default=0),
                      c: int = Header(default=None), timer: Any = Depends(loading)):
    return {"resultado: ": a + b, "Header": c}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000,  reload=True)