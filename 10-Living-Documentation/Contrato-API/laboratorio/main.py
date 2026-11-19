# COLA: código final da apresentação. Cada parte diz em que passo entra.
from enum import Enum                                   # [passo 5]

from fastapi import FastAPI                             # [passo 1]
from pydantic import BaseModel                          # [passo 2]

app = FastAPI(                                          # [passo 1] FastAPI(), [passo 6] title...
    title="Biblioteca API",
    description="API do seminário: o contrato nasce do código.",
    version="1.0.0",
)


class Genero(str, Enum):                                # [passo 5]
    ficcao = "ficcao"
    tecnico = "tecnico"
    biografia = "biografia"


class Livro(BaseModel):                                 # [passo 2]
    id: int
    titulo: str
    autor: str
    ano: int
    genero: Genero                                      # [passo 5]


# o "banco": uma lista simples                          # [passo 2] (genero entra no passo 5)
livros: list[Livro] = [
    Livro(id=1, titulo="Dom Casmurro", autor="Machado de Assis", ano=1899, genero="ficcao"),
]


# olá                                                   # [passo 1]
@app.get("/")
def raiz():
    return {"mensagem": "Olá, seminário!"}


# listar, com filtro opcional por gênero                # [passo 2], filtro no [passo 5]
@app.get("/livros")
def listar_livros() -> list[Livro]:
    return livros
    


# cadastrar: append                                     # [passo 2]
@app.post("/livros")
def criar_livro(livro: Livro) -> Livro:
    livros.append(livro)
    return livro


# buscar: se não achar, devolve None (vira null)       # [passo 3]
@app.get("/livros/{livro_id}")
def buscar_livro(livro_id: int) -> Livro | None:
    for livro in livros:
        if livro.id == livro_id:
            return livro


# atualizar: tira o antigo e põe o novo                 # [passo 3b]
@app.put("/livros/{livro_id}")
def atualizar_livro(livro_id: int, novo: Livro) -> Livro | None:
    for livro in livros:
        if livro.id == livro_id:
            livros.remove(livro)
            livros.append(novo)
            return novo


# remover                                               # [passo 3b]
@app.delete("/livros/{livro_id}")
def remover_livro(livro_id: int):
    for livro in livros:
        if livro.id == livro_id:
            livros.remove(livro)
            return {"mensagem": "Livro removido"}


from fastapi.staticfiles import StaticFiles
app.mount("/app", StaticFiles(directory="frontend", html=True))