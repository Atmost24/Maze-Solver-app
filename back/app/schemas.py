from pydantic import BaseModel, Field
from fastapi import UploadFile

class Item(BaseModel):
    maze: str

class fileRequest(BaseModel):
    file: UploadFile
    algorithm : str
    