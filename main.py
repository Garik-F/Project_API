from ast import List
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel
from pydantic import Field
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pymongo import MongoClient

app = FastAPI(
    title = "Trading App"
)

client = MongoClient("mongodb://localhost:27017/")
db = client["Users&Trides"]

DB_users = [
    {"id": 1, "role": "admin", "name": ["Bob"]},
    {"id": 2, "role": "investor", "name": "Igor"},
    {"id": 3, "role": "trador", "name": "Roman"},
    {"id": 4, "role": "trador", "name": "Vanya", "degree": [
        {"id": 6, "created_at": "2020-01-01T00:00:00", "type_degree": "expert"},
    ]},
]

class DegreeType(Enum):
    newbie = "newbie"
    expert = "expert"

class Degree(BaseModel):
    id: int
    created_at: datetime
    type_degree: DegreeType

class User(BaseModel):
    id: int
    role: str
    name: str
    degree: Optional[list[Degree]] = []

@app.get("/users/user_id", response_model=list[User])
def get_user(user_id: int):
    return [user for user in DB_users if user.get("id") == user_id]

DB_trades = [
    {"id": 1, "user_id": 1, "currency": "BTC", "side": "buy", "price": 123, "amount": 2.12},
    {"id": 2, "user_id": 1, "currency": "BTC", "side": "sell", "price": 345, "amount": 3.32},
]

@app.get("/trades")
def get_trades(limit: int = 1, offset: int = 0):
    return DB_trades[offset:][:limit]

DB_users2 = [
    {"id": 1, "role": "admin", "name": "Bob"},
    {"id": 2, "role": "investor", "name": "Igor"},
    {"id": 3, "role": "trador", "name": "Roman"},
]

@app.post("/users/{users_id}")
def change_user_name(user_id: int, new_name: str):
    current_user = list(filter(lambda user: user.get("id") == user_id, DB_users2))[0]
    current_user["name"] = new_name
    return {"status": 200, "data": current_user}

class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=5)
    side: str
    price: float = Field(ge=0)
    amount: float


@app.post("/trades")
def add_trades(trades: list[Trade]):
    DB_trades.extend(trades)
    return {"status": 200, "data": DB_trades}

@app.post("/users")
def add_users(users: list[User]):
    DB_users.extend(users)
    return {"status": 200, "data": DB_users}

def insert_user(name, role):
    users = db['users']
    user_data = {
        'name': name,
        'role': role
    }
    result = users.insert_one(user_data)
    print(f'Inserted user with ID {result.inserted_id}')

def insert_trides(user_id, side, price, amount):
    trides = db['trides']
    trides_data = {
        'user_id': user_id,
        'side': side,
        'price': price,
        'amount': amount
    }
    result = trides.insert_one(trides_data)
    print(f'Inserted order with ID {result.inserted_id}')


