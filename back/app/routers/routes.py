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

    result,allPath=deepSearch(0,1,maze,n,m)

    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()

    cMaze=convertMaze(maze)

    print(memory)
    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
            "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"profundidad"}

@router.post("/anchura")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    result,allPath=breadthSearch(0,1,maze,n,m)
    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()


    cMaze=convertMaze(maze)
    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
            "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"anchura"}


@router.post("/profundidad_iterativa")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    result,allPath=limitIterativeSearch(0,1,maze,n,m)
    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()

    cMaze=convertMaze(maze)
    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
            "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"profundidad iterativa"}


@router.post("/busqueda_uniforme")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    uniform=Uniform((0,1),(m-1,n-2),maze)
    cMaze,allPath,result=uniform.findPath()
    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()
    
    

    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
            "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"Uniforme"}

@router.post("/greedy")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    greedy=Greedy((0,1),(m-1,n-2),maze)
    cMaze,allPath,result=greedy.findPath()
    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()
    

    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
           "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"Greedy"}

@router.post("/a")
async def root(file: UploadFile):
    maze,n,m = read_maze(file.file)
    #n,m=options_maze(maze)
    #print(maze)
    start_time = time.time()
    tracemalloc.start()
    aStar=AStar((0,1),(m-1,n-2),maze)
    cMaze,allPath,result=aStar.findPath()
    memory=tracemalloc.get_traced_memory()
    totalTime=time.time() - start_time
    tracemalloc.stop()
    

    return {"pathResult": result,"allPath":allPath,"maze":cMaze,
            "memory":str(memory[1]/1000)+"KB","time":round(totalTime,6),"shape":f"{n},{m}","alg":"A*"}
