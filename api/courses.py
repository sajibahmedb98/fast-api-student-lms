from typing import Optional, List
from fastapi import FastAPI
import fastapi
from pydantic import BaseModel

router = fastapi.APIRouter()


@router.get("/courses")
async def get_courses():
    return {"courses": []}

@router.post("/courses")
async def create_course():
    return {"course": []}

@router.get("/courses/{id}")
async def get_course():
    return {"course": []}

@router.patch("/courses/{id}")
async def update_course():
    return {"course": []}

@router.delete("/courses/{id}")
async def delete_course():
    return {"course": []}