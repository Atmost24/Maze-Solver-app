import pandas as pd

def read_maze(csv):
    maze=pd.read_csv(csv,header=None).dropna().to_numpy()
    n,m=maze.shape
    return maze,n,m

def options_maze(maze):
    options_dict={}
    n,m=maze.shape
    for i in range(n):
        for j in range(m):
            if maze[i,j]=="w":
                continue
            options_dict[f"{i},{j}"]=[]
            #add left option
            if j!=0 and maze[i][j-1]!="w":
                options_dict[f"{i},{j}"].append("l")
            #add up option
            if i!=0 and maze[i-1][j]!="w":
                options_dict[f"{i},{j}"].append("u")
            #add right option
            if j<m-1 and maze[i][j+1]!="w":
                options_dict[f"{i},{j}"].append("r")
            #add down option
            if i<n-1 and maze[i+1][j]!="w":
                options_dict[f"{i},{j}"].append("d")
            
            
            
            

    return options_dict,n,m

def convertMaze(maze):
    return [list(map(lambda x: 0 if x=="c" else 1,i)) for i in maze]