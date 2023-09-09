from typing import Optional, List
from fastapi import FastAPI
from pydantic import BaseModel

from api import users, courses, sections


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


app.include_router(users.router)
app.include_router(courses.router)
app.include_router(sections.router)

