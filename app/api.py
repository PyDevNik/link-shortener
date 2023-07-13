from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse
import random

app = FastAPI()
links = []

def generate_id():
    def generate():
        return random.randint(100000, 999999)
    id = generate()
    while id in sum([list(l.keys()) for l in links], []):
        id = generate()
    return id


@app.get("/all")
def get_all_links():
    return JSONResponse(links)

@app.post("/add")
def add_link(link: str = Body()):
    if not link in sum([list(l.values()) for l in links], []):
        id = generate_id()
        links.append({id: link})
    return JSONResponse({id: link})

@app.get("/{id}")
def get_link(id: int):
    link = [l.get(id) for l in links][0]
    return JSONResponse({id: link}) if link else JSONResponse({"status": "Not found"})