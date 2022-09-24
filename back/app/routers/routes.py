from urllib.request import Request
from fastapi import APIRouter,UploadFile
from app.controller.controller import *
from app.schemas import *

import tracemalloc
import time


router = APIRouter(
    prefix="/classic",
    tags=["Classic"]
)

# @router.middleware("http")
# async def read_maze_before(req:Request,call_next):
#     maze = read_maze(req.maze.csv)
#     response = await call_next(maze)
#     return response

@router.get("/test")
async def root():
    return {"message": "testing"}

@router.post("/profundidad")
async def root(file: UploadFile):
    
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    result=deepSearch(0,1,maze,n,m)
    print(tracemalloc.get_traced_memory())
    print("--- %s seconds ---" % (time.time() - start_time))
    tracemalloc.stop()
    print(result)
    return {"message": result}

@router.post("/anchura")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    result=breadthSearch(0,1,maze,n,m)
    print(tracemalloc.get_traced_memory())
    print("--- %s seconds ---" % (time.time() - start_time))
    tracemalloc.stop()
    print(result)
    return {"message": result}

@router.post("/profundidad_iterativa")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    result=limitIterativeSearch(0,1,maze,n,m)
    print(tracemalloc.get_traced_memory())
    print("--- %s seconds ---" % (time.time() - start_time))
    tracemalloc.stop()
    print(result)
    
    return {"message": result}

@router.post("/busqueda_uniforme")
async def root(file: UploadFile):
    maze = read_maze(file.file)
    return {"message": "testing"}

@router.post("/greedy")
async def root(file: UploadFile):
    maze = read_maze(file.file)
    return {"message": "testing"}

@router.post("/a")
async def root(file: UploadFile):
    maze = read_maze(file.file)
    return {"message": "testing"}
