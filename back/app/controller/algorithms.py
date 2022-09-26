######all algorythms goes here
def pathValues(path):
    x=0
    y=1
    result=[{"x":y,"y":x}]
    for i in path:
        if i=="l" :
            y-=1
            result.append({"x":y,"y":x})
        elif i=="u" :
            x-=1
            result.append({"x":y,"y":x})
        elif i=="r":
            y+=1
            result.append({"x":y,"y":x})
        elif i=="d" : 
            x+=1
            result.append({"x":y,"y":x}) 
    return result

#deep-first algorithm
options=["l","u","r","d"]
def deepSearch(x,y,maze,n,m):
    result=""
    child=[[x,y]]
    allPath=[]
    val=["*"]
    while True:
        state=child.pop()
        act_val=val.pop()
        allPath.append({"x":state[1],"y":state[0]})
        last=act_val[-1]
        x=state[0]
        y=state[1]
        if x==n-1 and y==m-2:
            result=act_val[1:]
            result=pathValues(result)
            break
        for opt in options:
            if opt=="l" and "r"!=last and y>0 and maze[x][y-1]!="w":
                child.append([x,y-1])
                val.append(act_val+"l")
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
                child.append([x-1,y])
                val.append(act_val+"u")
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.append([x,y+1])
                val.append(act_val+"r")
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.append([x+1,y])
                val.append(act_val+"d")    
                  
    
    return result,allPath

#------- Breadth-first search

def breadthSearch(x,y,maze,n,m):
    result=""
    allPath=[]
    
    child=[[x,y]]
    val=["*"]
    while True:
        state=child.pop(0)
        act_val=val.pop(0)
        last=act_val[-1]
        x=state[0]
        y=state[1]
        allPath.append({"x":state[1],"y":state[0]})
        if x==n-1 and y==m-2:
            result=act_val[1:]
            result=pathValues(result)
            break
        for opt in options:
            if opt=="l" and "r"!=last and y>0 and maze[x][y-1]!="w":
                child.append([x,y-1])
                val.append(act_val+"l")
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
                child.append([x-1,y])
                val.append(act_val+"u")
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.append([x,y+1])
                val.append(act_val+"r")
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.append([x+1,y])
                val.append(act_val+"d")    
        
    
    return result,allPath

#------Depth-limited and iterative
def limitIterativeSearch(x,y,maze,n,m):
    allPath=[]
    result=""
    const=4
    limit=const
    child=[[x,y]]
    levels=[0]
    val=["*"]
    while True:
        state=child.pop()
        allPath.append({"x":state[1],"y":state[0]})
        act_val=val.pop()
        last=act_val[-1]
        actual_level=levels.pop()
        if actual_level==limit:
            limit+=const
        x=state[0]
        y=state[1]
        if x==n-1 and y==m-2:
            result=act_val[1:]
            result=pathValues(result)
            break

        pos=0 if act_val==limit else -1
        for opt in options:
            if opt=="l" and "r"!=last and y>0 and maze[x][y-1]!="w":
                
                child.insert(pos,[x,y-1])
                val.insert(pos,act_val+"l")
                levels.insert(pos,actual_level+1)
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
            
                child.insert(pos,[x-1,y])
                val.insert(pos,act_val+"u")
                levels.insert(pos,actual_level+1)
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.insert(pos,[x,y+1])
                val.insert(pos,act_val+"r")
                levels.insert(pos,actual_level+1)
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.insert(pos,[x+1,y])
                val.insert(pos,act_val+"d")   
                levels.insert(pos,actual_level+1) 
        
    
    return result,allPath

