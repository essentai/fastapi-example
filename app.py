from typing import Union, Optional
from fastapi import FastAPI, Path, Query, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    brand: Optional[str] = None

class UpdateItem(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = None
    brand: Optional[str] = None

class Poki(BaseModel):
    affiliation: str
    orientation: str
    number: Optional[int] = None

@app.get("/")
def read_root():
    return { "message": "Hello world!" }

@app.get("/about")
def about():
    return { "say": "I have nothing to say" }

inventory = {}
paul_sanders = {}

@app.get("/get-by-name")
def get_item(*, name: Optional[str] = None, test: int):
    for item_id in inventory:
        if inventory[item_id].name == name:
            return inventory[item_id]
    raise HTTPException(status_code=404, detail="Item ID not found.")

@app.post("/create-item/{item_id}")
def create_item(item_id: int, item: Item):
    if item_id in inventory:
        raise HTTPException(status_code=400, detail="Item ID already exists.")
    inventory[item_id]= item
    return inventory[item_id]

@app.put("/update-item/{item_id}")
def update_item(item_id: int, item: UpdateItem):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID not found.")
    if item.name != None:
        inventory[item_id].name = item.name
    if item.price != None:
        inventory[item_id].price = item.price
    if item.brand != None:
        inventory[item_id].brand = item.brand
    return inventory[item_id]

@app.delete("/delete-item")
def delete_item(item_id: int = Query(..., description="The IDf the item gt = 0")):
    if item_id not in inventory:
        raise HTTPException(status_code=404, detail="Item ID not found.")
    del inventory[item_id]
    return {"Success": "Item succesfully deleted."}
