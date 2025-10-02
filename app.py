from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Dict

app = FastAPI()

class Tarefa(BaseModel):
    nome: str
    descricao: str
    concluida: bool = False

lista_tarefas: List[Dict] = []

@app.post("/tarefas/", status_code=201)
def adicionar_tarefas(tarefa: Tarefa):
    lista_tarefas.append(tarefa.model_dump())
    return {"message": "Tarefa adicionada com sucesso!", "Tarefa": tarefa}

@app.get("/tarefas/")
def lista_tarefa():
    return {"tarefas": lista_tarefas}

@app.put("/tarefas/{nome_tarefa}")
def marcar_tarefa_concluida(nome_tarefa: str):
    for tarefa in lista_tarefas:
        if tarefa["nome"] == nome_tarefa:
            tarefa["concluida"] = True
            return {"message": f"Tarefa '{nome_tarefa}' concluída com sucesso!", "Tarefa": tarefa}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")

@app.delete("/tarefas/{nome_tarefa}")
def remover_tarefa(nome_tarefa: str):
    for tarefa in lista_tarefas:
        if tarefa["nome"] == nome_tarefa:
            lista_tarefas.remove(tarefa)
            return {"message": "Tarefa deletada com sucesso!"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada.")
