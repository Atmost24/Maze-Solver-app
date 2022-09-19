from pydantic import BaseModel, Field
from fastapi import File

class Item(BaseModel):
    maze: str
    