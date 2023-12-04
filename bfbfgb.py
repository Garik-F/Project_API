from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

app = FastAPI()

# Подключение к MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]

# Модель для пользователя
class User(BaseModel):
    username: str
    email: str

# Модель для заказа
class Order(BaseModel):
    user_id: str
    product: str
    quantity: int

# Создание пользователя
@app.post("/users/")
async def create_user(user: User):
    collection = db["users"]
    result = collection.insert_one(user.dict())
    return {"id": str(result.inserted_id), "username": user.username, "email": user.email}

# Получение пользователя по ID
@app.get("/users/{user_id}")
async def get_user(user_id: str):
    collection = db["users"]
    user = collection.find_one({"_id": user_id})
    if user:
        return user
    raise HTTPException(status_code=404, detail="User not found")

# Создание заказа
@app.post("/orders/")
async def create_order(order: Order):
    collection = db["orders"]
    result = collection.insert_one(order.dict())
    return {"id": str(result.inserted_id), "user_id": order.user_id, "product": order.product, "quantity": order.quantity}