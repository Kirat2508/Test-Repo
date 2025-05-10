from fastapi import FastAPI, HTTPException, Depends, status
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
from datetime import datetime

# Initialize FastAPI app
app = FastAPI(
    title="Sample API",
    description="A sample API built with FastAPI",
    version="1.0.0"
)

# Create a data model using Pydantic
class Item(BaseModel):
    id: Optional[int] = None
    name: str
    description: Optional[str] = None
    price: float
    is_available: bool = True
    created_at: datetime = datetime.now()

    class Config:
        schema_extra = {
            "example": {
                "name": "Laptop",
                "description": "A high-performance laptop",
                "price": 999.99,
                "is_available": True
            }
        }

# In-memory database
items_db = []
item_id_counter = 1

# Root endpoint
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to the Sample API"}

# Create an item
@app.post("/items/", response_model=Item, status_code=status.HTTP_201_CREATED, tags=["Items"])
async def create_item(item: Item):
    global item_id_counter
    item.id = item_id_counter
    items_db.append(item.dict())
    item_id_counter += 1
    return item

# Get all items
@app.get("/items/", response_model=List[Item], tags=["Items"])
async def get_items(skip: int = 0, limit: int = 10):
    return items_db[skip: skip + limit]

# Get a specific item by ID
@app.get("/items/{item_id}", response_model=Item, tags=["Items"])
async def get_item(item_id: int):
    for item in items_db:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# Update an item
@app.put("/items/{item_id}", response_model=Item, tags=["Items"])
async def update_item(item_id: int, updated_item: Item):
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            # Keep the original ID
            updated_item.id = item_id
            # Update the item in the database
            items_db[i] = updated_item.dict()
            return updated_item
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# Delete an item
@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT, tags=["Items"])
async def delete_item(item_id: int):
    for i, item in enumerate(items_db):
        if item["id"] == item_id:
            items_db.pop(i)
            return
    raise HTTPException(status_code=404, detail=f"Item with ID {item_id} not found")

# Health check endpoint
@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "healthy", "timestamp": datetime.now()}

# Run the application
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
