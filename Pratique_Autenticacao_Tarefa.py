from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from pydantic import BaseModel
from typing import Optional
import secrets

app = FastAPI()

MY_USERNAME = "admin"
MY_PASSWORD = "adminadmin"

security = HTTPBasic()


class Tarefa(BaseModel):
    #id: int
    nome: str
    descricao: str

listar_tarefas = []

def autenticar_my_username(credentials: HTTPBasicCredentials = Depends(security)):
    is_username_correct = secrets.compare_digest(credentials.username, MY_USERNAME)
    is_password_correct = secrets.compare_digest(credentials.password, MY_PASSWORD)

    if not (is_username_correct and is_password_correct):
        raise HTTPException(
            status_code=401,
            detail="Usuário e senha incorretos",
            headers={"WWW-Autheticate": "Basic"}
        )


@app.get("/tarefa")
def get_tarefas(page: int = 1, limit: int = 5, credentials: HTTPBasicCredentials = Depends(autenticar_my_username)):
    if page < 1 or limit < 1:
        raise HTTPException(status_code=400, detail="Page ou limit inválidos.")
    
    if not listar_tarefas:
        return {"message": "Não existe nenhuma tarefa registrada."}
    
    ordenar_tarefas = sorted(listar_tarefas, key=lambda tarefa: tarefa.nome)


    start = (page - 1) * limit
    end = start + limit

    tarefas_paginadas = ordenar_tarefas[start:end]
    return {
        "page": page,
        "limit": limit,
        "total": len(listar_tarefas),
        "tarefas": [tarefa.dict() for tarefa in tarefas_paginadas]
    }


@app.post("/tarefa", status_code=201)
def add_tarefas(tarefa: Tarefa, credentials: HTTPBasicCredentials = Depends(autenticar_my_username)):
    for t in listar_tarefas:
        if t.nome == tarefa.nome:
            raise HTTPException(status_code=400, detail= "Essa tarefa já foi registrada.")
    listar_tarefas.append(tarefa)
    return {"message": "Tarefa adicionada com sucesso", "Tarefa":tarefa}

@app.put("/tarefa/atualizar/{nome}")
def atualizar_tarefa(nome: str, nova_tarefa: Tarefa, credentials: HTTPBasicCredentials = Depends(autenticar_my_username)):
    for atu, tarefa in enumerate(listar_tarefas):
        if tarefa.nome == nome:
            listar_tarefas[atu] = nova_tarefa
            return {"message": f"Tarefa '{nome}' concluida com sucesso.", "Tarefa": nova_tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefa/{nome}")
def remover_tarefa(nome: str, credentials: HTTPBasicCredentials = Depends(autenticar_my_username)):
    for tarefa in listar_tarefas:
        if tarefa.nome == nome:
            listar_tarefas.remove(tarefa)
            return {"message": "Tarefera removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada") 