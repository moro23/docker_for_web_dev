## app/main.py
from fastapi import FastAPI

app = FastAPI(title="FastAPI, Docker, and Traefik")

@app.get("/")
def read_home():
    return {'hello-World!'}


