######all algorythms goes here
import graphviz
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
    graph=True if n<=10 and m<=10 else False
    
    result=""
    child=[[x,y]]
    allPath=[]
    val=["*"]
    count=-1
    if graph:
        f = graphviz.Digraph('a', format='png')
        f.attr(bgcolor='#282C34')
        f.attr('node',fontcolor='#F9F9F9')
        f.attr('node',color='#F9F9F9')
        f.attr('edge',color='#F9F9F9')
        idNum=[0]
    
    while True:
   
        
        count+=1
        state=child.pop()
        act_val=val.pop()
        allPath.append({"x":state[1],"y":state[0]})
        last=act_val[-1]
        if graph:
            lastId=idNum.pop()
            if last=="*":
                f.node(f'{lastId}', f'{last}')
            else:
                f.node(f'{count}', f'{last}')
                f.edge(str(lastId),str(count))
                lastId=count
        
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
                if graph:
                    idNum.append(lastId)
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
                child.append([x-1,y])
                val.append(act_val+"u")
                if graph:
                    idNum.append(lastId)
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.append([x,y+1])
                val.append(act_val+"r")
                if graph:
                    idNum.append(lastId)
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.append([x+1,y])
                val.append(act_val+"d")   
                if graph: 
                    idNum.append(lastId)
    if graph:
        f.render().replace('\\', '/')
    return result,allPath

#------- Breadth-first search

import graphviz
def breadthSearch(x,y,maze,n,m):
    graph=True if n<=10 and m<=10 else False
    result=""
    allPath=[]
    child=[[x,y]]
    val=["*"]
    count=-1
    if graph:
        f = graphviz.Digraph('a', format='png')
        f.attr(bgcolor='#282C34')
        f.attr('node',fontcolor='#F9F9F9')
        f.attr('node',color='#F9F9F9')
        f.attr('edge',color='#F9F9F9')
    idNum=[0]
    while True:

        count+=1
        state=child.pop(0)
        act_val=val.pop(0)
        last=act_val[-1]
        x=state[0]
        y=state[1]
        allPath.append({"x":state[1],"y":state[0]})
        if graph:
            lastId=idNum.pop(0)
            if last=="*":
                f.node(f'{lastId}', f'{last}')
            else:
                f.node(f'{count}', f'{last}')
                f.edge(str(lastId),str(count))
                lastId=count
        if x==n-1 and y==m-2:
            result=act_val[1:]
            result=pathValues(result)
            break
        for opt in options:
            if opt=="l" and "r"!=last and y>0 and maze[x][y-1]!="w":
                child.append([x,y-1])
                val.append(act_val+"l")
                if graph:
                    idNum.append(count)
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
                child.append([x-1,y])
                val.append(act_val+"u")
                if graph:
                    idNum.append(count)
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.append([x,y+1])
                val.append(act_val+"r")
                if graph:
                    idNum.append(count)
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.append([x+1,y])
                val.append(act_val+"d")
                if graph: 
                    idNum.append(count)   
        
    if graph:
        f.render().replace('\\', '/')
    return result,allPath

#------Depth-limited and iterative
def limitIterativeSearch(x,y,maze,n,m,l):
    graph=True if n<=10 and m<=10 else False
    allPath=[]
    result=""
    const=l
    limit=const
    child=[[x,y]]
    levels=[0]
    val=["*"]
    count=-1
    if graph :
        f = graphviz.Digraph('a', format='png')
        f.attr(bgcolor='#282C34')
        f.attr('node',fontcolor='#F9F9F9')
        f.attr('node',color='#F9F9F9')
        f.attr('edge',color='#F9F9F9')
    idNum=[0]
    while True:
        #print(child,levels)
        count+=1
        state=child.pop()
        allPath.append({"x":state[1],"y":state[0]})
        act_val=val.pop()
        last=act_val[-1]
        actual_level=levels.pop()
        
        if graph:
            lastId=idNum.pop()
            if last=="*":
                f.node(f'{lastId}', f'{last}')
            else:
                f.node(f'{count}', f'{last}')
                f.edge(str(lastId),str(count))
                lastId=count
        if actual_level==limit:
            limit+=const
        x=state[0]
        y=state[1]
        if x==n-1 and y==m-2:
            result=act_val[1:]
            result=pathValues(result)
            break

        posFlag=0 if actual_level+1==limit else -1
        for opt in options:
            pos=len(child) if posFlag==-1 else 0
            if opt=="l" and "r"!=last and y>0 and maze[x][y-1]!="w":
                child.insert(pos,[x,y-1])
                val.insert(pos,act_val+"l")
                levels.insert(pos,actual_level+1)
                if graph:
                    idNum.insert(pos,count)
            elif opt=="u" and "d"!=last and x>0 and maze[x-1][y]!="w":
            
                child.insert(pos,[x-1,y])
                val.insert(pos,act_val+"u")
                levels.insert(pos,actual_level+1)
                if graph:
                    idNum.insert(pos,count)
            elif opt=="r" and "l"!=last and y<m-1 and maze[x][y+1]!="w":
                child.insert(pos,[x,y+1])
                val.insert(pos,act_val+"r")
                levels.insert(pos,actual_level+1)
                if graph:
                    idNum.insert(pos,count)
            elif opt=="d" and "u"!=last and x<n-1 and maze[x+1][y]!="w": 
                child.insert(pos,[x+1,y])
                val.insert(pos,act_val+"d")   
                levels.insert(pos,actual_level+1) 
                if graph:
                    idNum.insert(pos,count)
        
    if graph:
        f.render().replace('\\', '/')
    return result,allPath
