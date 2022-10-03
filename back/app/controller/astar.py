from heapq import heappop, heappush
import random
import sys
from app.controller.specialTuple import Tup
from app.controller.maze_solver import convertMaze

class AStar:
    def __init__(self, origin, goal, maze):
        self.allPaths = []
        self.maze = maze
        self.height = len(self.maze)
        self.width = len(self.maze[0])
        if self.isInRange(goal):
            self.goal = goal
        else:
            self.goal = (self.height - 1, self.width - 1)
        if self.isInRange(origin):
            self.origin = origin
        else:
            self.origin = (0, 0)    
    def isInRange(self,cell):
        return cell[0] <= self.height and cell[0] >= 0 and cell[1] <= self.width and cell[1] >= 0
    def d(self, start, final):
        return abs(start[0] - final[0]) + abs(start[1] - final[1])
    def h(self, cell):
        return abs(cell[0] - self.goal[0]) + abs(cell[1] - self.goal[1])
    def calculeNeighborhood(self, cell):
        neighbours = []
        row, col = cell[0], cell[1]
        if row - 1 >= 0:
            neighbours.append((row - 1,col))
        if row + 1 < self.height:
            neighbours.append((row + 1,col))
        if col - 1 >= 0:
            neighbours.append((row, col - 1))
        if col + 1 < self.width:
            neighbours.append((row, col + 1))
        pathNeighbours = []
        for neighbour in neighbours:
            if self.maze[neighbour[0]][neighbour[1]] == "c":
                pathNeighbours.append(neighbour)
        random.shuffle(pathNeighbours)
        return pathNeighbours  
    def getPath(self, cameFrom, current):
        path = [{"x":current[1],"y": current[0]}]
        while current!= None and cameFrom[current[0]][current[1]] != None:
            current = cameFrom[current[0]][current[1]]
            path.append({"x":current[1],"y": current[0]})
        return path[::-1]
    def findPath(self):
        cameFrom = [[ None for col in range(self.width)] for row in range(self.height)]
        g = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        g[self.origin[0]][self.origin[1]] = 0
        f = [[ sys.maxsize for col in range(self.width)] for row in range(self.height)]
        f[self.origin[0]][self.origin[1]] = self.h((self.origin[0],self.origin[1]))
        openSet = []
        listAllPaths=[]
        heappush(openSet, Tup(f[self.origin[0]][self.origin[1]], self.origin))
        while len(openSet) > 0:
            currCell = heappop(openSet).getPair()
            #self.allPaths.append(self.getPath(cameFrom, currCell))
            listAllPaths.append({"x":currCell[1],"y": currCell[0]})
            if currCell == self.goal:
                return convertMaze(self.maze), listAllPaths, self.getPath(cameFrom, currCell)
            neighbours = self.calculeNeighborhood(currCell)
            for neighbour in neighbours:
                preG = g[currCell[0]][currCell[1]] + self.d(currCell, neighbour)
                if preG < g[neighbour[0]][neighbour[1]]:
                    preNeighbour = Tup(f[neighbour[0]][neighbour[1]],  neighbour)
                    cameFrom[neighbour[0]][neighbour[1]] = currCell
                    g[neighbour[0]][neighbour[1]] = preG
                    f[neighbour[0]][neighbour[1]] = preG + self.h(neighbour)
                    if preNeighbour not in openSet:
                        heappush(openSet, Tup(f[neighbour[0]][neighbour[1]], neighbour))
        return False