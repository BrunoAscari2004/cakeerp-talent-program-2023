from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class Curso(Base):
    __tablename__ = "cursos"

    id: int = Column(Integer, primary_key=True, index=True)
    titulo: str = Column(String(100), nullable=False)
    descricao: str = Column(String(255), nullable=False)
    carga_horaria: int = Column(Integer, nullable=False)
    qtd_exercicios: int = Column(Integer, nullable=False)
    active: Column(Boolean, default=True )

    alunos = relationship("Aluno", back_populates="curso")

'''2. criar um novo modelo chamado aluno com os seguintes atributos id, nome, sobrenome, email, idade, cpf e id_curso(obs. o aluno so poderá se associar a um único curso)
'''

class Aluno(Base):
    __tablename__ = "alunos"

    id: int = Column(Integer, primary_key=True, index=True)
    nome: str = Column(String(100),nullable=False)
    sobrenome: str= Column(String(100),nullable=False)
    email: str=Column(String(100),nullable=True)
    idade: int=Column(Integer,nullable=True)
    cpf: str=Column(String(100),nullable=False,unique=True)
    id_curso: int = Column(Integer, ForeignKey('cursos.id'),nullable=False)

    curso = relationship("Curso", back_populates="alunos")
