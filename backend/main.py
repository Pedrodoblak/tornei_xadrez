from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"mensagem": "Seu Torneio de Xadrez está online!"}
