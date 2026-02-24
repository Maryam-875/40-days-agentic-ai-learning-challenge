from fastapi import FastAPI, HTTPException
from uuid import uuid4

app = FastAPI()
db = {}

@app.post("/items/")
def create_item(name: str, description: str = None):
    item_id = str(uuid4())
    db[item_id] = {"name": name, "description": description}
    return {**db[item_id], "id": item_id}

@app.get("/items/")
def read_items():
    return db

@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    return {**db[item_id], "id": item_id}

@app.put("/items/{item_id}")
def update_item(item_id: str, name: str, description: str = None):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    db[item_id] = {"name": name, "description": description}
    return {**db[item_id], "id": item_id}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item not found")
    del db[item_id]
    return {"detail": "Item deleted"}
