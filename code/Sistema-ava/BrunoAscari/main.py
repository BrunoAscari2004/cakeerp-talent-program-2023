from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session
from fastapi.openapi.utils import get_openapi
from models import Curso
from models import Aluno
from database import engine, Base, get_db
from repositories import CursoRepository
from repositories import AlunoRepository
from schemas import CursoRequest, CursoResponse
from schemas import AlunoRequest, AlunoResponse

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/api/cursos", response_model=CursoResponse, status_code=status.HTTP_201_CREATED)
def create(request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.save(db, Curso(**request.dict()))
    return CursoResponse.from_orm(curso)

@app.get("/api/cursos", response_model=list[CursoResponse])
def find_all(db: Session = Depends(get_db)):
    cursos = CursoRepository.find_all(db)
    return [CursoResponse.from_orm(curso) for curso in cursos]

@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.get("/api/cursos/{curso_id}", response_model=CursoResponse)
def find_curso_by_id(curso_id: int, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    return CursoResponse.from_orm(curso)


@app.delete("/api/cursos/{curso_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_curso(curso_id: int, db: Session = Depends(get_db)):
    if not CursoRepository.exists_by_id(db, curso_id):
        raise HTTPException(status_code=404, detail="Curso não encontrado")
    CursoRepository.delete_by_id(db, curso_id)

@app.put("/api/cursos/{curso_id}", response_model=CursoResponse)
def update_curso(curso_id: int, request: CursoRequest, db: Session = Depends(get_db)):
    curso = CursoRepository.find_by_id(db, curso_id)
    if curso is None:
        raise HTTPException(status_code=404, detail="Curso não encontrado")

    
    for atributo, value in request.dict().items():
        setattr(curso, atributo, value)
    
   
    CursoRepository.save(db, curso)
    
    return CursoResponse.from_orm(curso)




def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Ambiente Virtual de Aprendizagem",
        version="1.0.0",
        summary="Alunos EAD",
        description="Sistema de Ambiente Virtual de Aprendizagem para auxiliar alunos 100% EAD",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app.openapi = custom_openapi


'''Para alunos'''

@app.post("/api/alunos", response_model=AlunoResponse, status_code=status.HTTP_201_CREATED)
def create(request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.save_aluno(db, Aluno(**request.dict()))
    return AlunoResponse.from_orm(aluno)

@app.get("/api/alunos", response_model=list[AlunoResponse])
def find_all_alunos(db: Session = Depends(get_db)):
    alunos = AlunoRepository.find_all_alunos(db)
    return [AlunoResponse.from_orm(aluno) for aluno in alunos]



@app.get("/api/alunos/{aluno_id}", response_model=AlunoResponse)
def find_aluno_by_id(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_alunos_by_id(db, aluno_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno  não encontrado")
    return AlunoResponse.from_orm(aluno)


@app.delete("/api/alunos/{aluno_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_aluno(aluno_id: int, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_alunos_by_id(db, aluno_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="aluno não encontrado")

    curso_id = aluno.id_curso
    curso = CursoRepository.find_by_id(db, curso_id)

    if curso.active:
        raise HTTPException(status_code=400, detail="nao foi possível excluir o aluno, pois ele está vinculado a um curso ativo")

    AlunoRepository.delete_by_aluno_id(db, aluno_id)


@app.put("/api/alunos/{aluno_id}", response_model=AlunoResponse)
def update_aluno(aluno_id: int, request: AlunoRequest, db: Session = Depends(get_db)):
    aluno = AlunoRepository.find_by_id(db, aluno_id)
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")

    
    for atributo, value in request.dict().items():
        setattr(aluno, atributo, value)
    
   
    CursoRepository.save(db, aluno)
    
    return CursoResponse.from_orm(aluno)