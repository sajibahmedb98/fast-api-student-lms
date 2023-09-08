from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI(
    title="FastAPI LMS",
    description="LMS API for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Sajib Ahmed",
        "email": "sajibahmed294@gmail.com",
    },
    license_info={
        "name": "MIT",
    }
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users")
async def get_users(response_model=List[User]):
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "User created"


@app.get("/users/{id}")
async def get_user(id: int):
    return {"user": users[id]}
