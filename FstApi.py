from fastapi import FastAPI, Request
from pydantic import BaseModel


app = FastAPI()

perfis = {
    1: {"Nome" : "André", "Idade" : "15", "Profissão" : "Desempregado"},
    2: {"Nome" : "Matheus", "Idade" : "20", "Profissão" : "Aprendiz de Ferreiro"},
    3: {"Nome" : "Carmélia", "Idade" : "70", "Profissão" : "Artesã"},
    4: {"Nome" : "Raimundo", "Idade" : "127", "Profissão" : "Ancião"},
    5: {}
}

class User(BaseModel):
    Nome: str
    Idade: int
    Profissão: str

@app.get("/")

#Status da Api.

def home():
    return "Funcionando"
@app.get("/users")
def users_menu():
    return f"Temos {len(perfis)} usuários: \n{perfis}\n digite o ID do que você quer acessar sua conta."

@app.get("/users/{id_user}")

#Pega usuários.

def get_users(id_user : int):
    return {"User" : perfis[id_user]}

@app.post("/users/criar/{id_user}")

#Cria usuários.

async def criar(user : User, id_user):
    if perfis[id_user] == {}:
        perfis.update(perfis[id_user : {user}])
        return user
    else:
        return {"message":"O usuário de id {id_user} já exsite"}