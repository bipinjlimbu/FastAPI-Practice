from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()

@app.post("/users", status_code=status.HTTP_201_CREATED)
def create_user(user: dict):
    return {
        "message": "User created successfully",
        "user": user
    }
    
@app.get("/users/")
def get_users():
    return {
        "status": "success",
        "message": "Users retrieved successfully",
        "data": [
            {"id": 1, "name": "Alice"},
            {"id": 2, "name": "Bob"}
        ]
    }