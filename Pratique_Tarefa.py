from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Tarefa(BaseModel):
    id: int
    nome: str
    descricao: str
    concluida: bool = False

listar_tarefas: list[Tarefa] = []

@app.post("/tarefa/", status_code=201)
def adicionar_tarefa(tarefa: Tarefa):
    listar_tarefas.append(tarefa)
    return {"message" : "Tarefa adicionada com sucesso!", "Tarefa": tarefa}

@app.put("/tarefa/concluir/{nome}")
def tarefa_concluida(nome: str):
    for tarefa in listar_tarefas:
        if tarefa.nome == nome:
            tarefa.concluida = True
            return {"message": f"Tarefa '{nome}' concluída com sucesso!", "Tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.get("/tarefa/{id}", response_model=Tarefa)
def buscar_tarefas(id: int):
    for tarefa in listar_tarefas:
        if tarefa.id == id:
            return tarefa
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tarefa/{nome}")
def remover_tarefa(nome: str):
    for tarefa in listar_tarefas:
        if tarefa.nome == nome:
            listar_tarefas.remove(tarefa)
            return {"message": "Tarefa deletada com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
