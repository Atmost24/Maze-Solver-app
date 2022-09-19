######all algorythms goes here


#deep-first algorithm

def deepSearch(x,y,opt_maze,n,m):
    result=""
    
    child=[[x,y]]
    val=["*"]
    while True:
        state=child.pop()
        act_val=val.pop()
        last=act_val[-1]
        x=state[0]
        y=state[1]
        if x==n-1 and y==m-2:
            result=act_val
            break
        for opt in opt_maze[f"{x},{y}"]:
            if opt=="d" and "u"!=last:
                child.append([x+1,y])
                val.append(act_val+"d")
            if opt=="r" and "l"!=last:
                child.append([x,y+1])
                val.append(act_val+"r")
            if opt=="u" and "d"!=last:
                child.append([x-1,y])
                val.append(act_val+"u")
            if opt=="l" and "r"!=last:
                child.append([x,y-1])
                val.append(act_val+"l")
    
    return result


