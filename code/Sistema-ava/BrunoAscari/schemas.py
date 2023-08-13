from pydantic import BaseModel

class CursoBase(BaseModel):
    titulo: str
    descricao: str
    carga_horaria: int
    qtd_exercicios: int

class CursoRequest(CursoBase):
    ...

class CursoResponse(CursoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True


'''Aluno'''
class AlunoBase(BaseModel):
    id: int 
    nome: str
    sobrenome: str
    idade: int
    cpf: str

class AlunoRequest(AlunoBase):
    ...

class AlunoResponse(AlunoBase):
    id: int

    class Config:
        from_attributes = True
        orm_mode = True