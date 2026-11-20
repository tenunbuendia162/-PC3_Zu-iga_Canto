from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False

# Diccionario en memoria para guardar los ítems {id: Item}
items_db: dict[int, Item] = {}
next_id = 1

@app.post("/items/")
def create_item(item: Item):
    global next_id
    item_id = next_id
    items_db[item_id] = item
    next_id += 1
    return {"item_id": item_id, "item": item}

@app.get("/items/")
def read_all_items():
    return items_db

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    if item_id not in items_db:
        raise HTTPException(status_code=404, detail="Item no encontrado")
    return {"item_id": item_id, "item": items_db[item_id], "q": q}