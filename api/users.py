from typing import Optional, List
from fastapi import FastAPI
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]

# get all users
@router.get("/users")
async def get_users(response_model=List[User]):
    return users

# create a user
@router.post("/users")
async def create_user(user: User):
    users.append(user)
    return "User created"

# get a user
@router.get("/users/{id}")
async def get_user(id: int):
    return {"user": users[id]}
