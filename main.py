from fastapi import FastAPI

# Membuat instance FastAPI
app = FastAPI()

# Endpoint dengan metode GET
@app.get("/")
def read_root():
    return {"message": "Selamat datang di API Python Anda!", "method": "GET"}

# Endpoint GET lain dengan Path Parameter
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "query": q, "message": "Detail Item"}
