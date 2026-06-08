from typing import List, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

items: List[Item] = []

@app.get("/", summary="API health check")
def read_root():
    return {"message": "FastAPI REST API is running"}

@app.get("/items", response_model=List[Item])
def list_items():
    return items

@app.post("/items", response_model=Item, status_code=201)
def create_item(item: Item):
    if any(existing.id == item.id for existing in items):
        raise HTTPException(status_code=400, detail="Item with this id already exists")
    items.append(item)
    return item

@app.get("/items/{item_id}", response_model=Item)
def get_item(item_id: int):
    for item in items:
        if item.id == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.put("/items/{item_id}", response_model=Item)
def update_item(item_id: int, item: Item):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            items[index] = item
            return item
    raise HTTPException(status_code=404, detail="Item not found")

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    for index, existing in enumerate(items):
        if existing.id == item_id:
            del items[index]
            return {"message": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
