from typing import List
from fastapi import APIRouter, Depends, Response, status
from fastapi import HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from models.curso_model import CursoModel
from schemas.curso_schema import CursoSchema
from core.deps import getSession

router = APIRouter()

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=CursoSchema)
async def createCurso(curso: CursoSchema, db: AsyncSession = Depends(getSession)):
    novoCurso = CursoModel(titulo=curso.titulo, aulas=curso.aulas, horas=curso.horas)
    db.add(novoCurso)
    await db.commit()
    return novoCurso

@router.get('/', response_model=List[CursoSchema])
async def getCursos(db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(CursoModel)
        result = await session.execute(query)
        cursos: List = result.scalars().all()
        return cursos
    
@router.get('/{cursoId}', response_model=CursoSchema)
async def getCurso(cursoId: int, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == cursoId)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            return curso
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")


@router.put('/{cursoId}', response_model=CursoSchema, status_code=status.HTTP_202_ACCEPTED)
async def editCurso(cursoId: int, curso: CursoSchema, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == cursoId)
        result = await session.execute(query)
        cursoDB = result.scalar_one_or_none()
        if cursoDB:
            cursoDB.titulo = curso.titulo
            cursoDB.aulas = curso.aulas
            cursoDB.horas = curso.horas
            await db.commit()
            return cursoDB
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")
   
    
@router.delete('/{cursoId}', status_code=status.HTTP_200_OK)
async def deleteCurso(cursoId: int, db: AsyncSession = Depends(getSession)):
    async with db as session:
        query = select(CursoModel).where(CursoModel.id == cursoId)
        result = await session.execute(query)
        curso = result.scalar_one_or_none()
        if curso:
            await session.delete(curso)
            await db.commit()
            return Response(status_code=status.HTTP_200_OK)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Curso não encontrado")