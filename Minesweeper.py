import random
import numpy as np
import math

grid = []
nom = 0

length = 14
height = length
#will work on rectangles later

difficultyfactor = 10
#difficulty too

nom = 0

for i in range(length*height):
    x = 1
    if x == random.randint(0,3):
        grid.append(1)
        nom +=1
    else:
        grid.append(0)
        



grid = np.array(grid)
grid.shape = (height,length)

#print(grid)


y = 0
newgrid = []
for row in grid:
    x = 0
    
    for space in row:
        if space == 0:
            #print("free",x,y)
            if x == length -1  and y== height - 1:
                #print("bot right")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x-1])+int(grid[y,x-1]))
            elif x == 0 and y== height - 1:
                #print("bot left")
                newgrid.append(int(grid[y,x+1])+int(grid[y-1,x])+int(grid[y-1,x+1]))
            elif x == length -1 and y == 0:
                #print("top right")
                newgrid.append(int(grid[y+1,x])+int(grid[y+1,x-1])+int(grid[y,x-1]))
            elif x == 0 and y== 0:
                #print("top left")
                newgrid.append(int(grid[y,x+1])+int(grid[y+1,x])+int(grid[y+1,x+1]))
            elif x == 0:
                #print("left")
                newgrid.append(int(grid[y,x+1]+int(grid[y+1,x+1])+int(grid[y+1,x])+int(grid[y-1,x])+int(grid[y-1,x+1])))
            elif y == 0:
                #print("top")
                newgrid.append(int(grid[y+1,x])+int(grid[y+1,x+1])+int(grid[y+1,x-1])+int(grid[y,x+1])+int(grid[y,x-1]))
                
            elif y == height - 1:
                #print("bot")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x+1])+int(grid[y-1,x-1])+int(grid[y,x+1])+int(grid[y,x-1]))
            elif x == length -1:
                #print("right")
                newgrid.append(int(grid[y,x-1]+int(grid[y+1,x-1])+int(grid[y+1,x])+int(grid[y-1,x]+int(grid[y-1,x-1]))))
            else:
                #print("middle")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x-1])+int(grid[y-1,x+1])+int(grid[y,x-1])+int(grid[y,x+1])+int(grid[y+1,x])+int(grid[y+1,x+1])+int(grid[y+1,x-1]))
            
        
        else:
            #print(grid[y,x],"coords:",x,y,"mine")
            newgrid.append("X")
        x+=1
        #print("next row")
        
    y+=1
    
#print(grid,"old")
newgrid = np.array(newgrid)
newgrid.shape = (length, height)

#print(newgrid,"new")
print("number of mines: ", nom)
print("board size:", length*height)

shownboard = []
for i in range(length*height):
    shownboard.append("■")
shownboard = np.array(shownboard)
shownboard.shape = (length, height)
print(shownboard)

running = True
sx = int(input("x: "))
sy = int(input("y: "))
grid[sy,sx] = 0
grid[sy-1,sx] = 0
grid[sy-1,sx+1] = 0
grid[sy-1,sx-1] = 0
grid[sy+1,sx-1] = 0
grid[sy,sx-1] = 0
grid[sy+1,sx] = 0
grid[sy+1,sx+1] = 0
grid[sy,sx+1] = 0



newgrid = []
y = 0
for row in grid:
    x = 0
    
    for space in row:
        if space == 0:
            #print("free",x,y)
            if x == length -1  and y== height - 1:
                #print("bot right")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x-1])+int(grid[y,x-1]))
            elif x == 0 and y== height - 1:
                #print("bot left")
                newgrid.append(int(grid[y,x+1])+int(grid[y-1,x])+int(grid[y-1,x+1]))
            elif x == length -1 and y == 0:
                #print("top right")
                newgrid.append(int(grid[y+1,x])+int(grid[y+1,x-1])+int(grid[y,x-1]))
            elif x == 0 and y== 0:
                #print("top left")
                newgrid.append(int(grid[y,x+1])+int(grid[y+1,x])+int(grid[y+1,x+1]))
            elif x == 0:
                #print("left")
                newgrid.append(int(grid[y,x+1]+int(grid[y+1,x+1])+int(grid[y+1,x])+int(grid[y-1,x])+int(grid[y-1,x+1])))
            elif y == 0:
                #print("top")
                newgrid.append(int(grid[y+1,x])+int(grid[y+1,x+1])+int(grid[y+1,x-1])+int(grid[y,x+1])+int(grid[y,x-1]))
                
            elif y == height - 1:
                #print("bot")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x+1])+int(grid[y-1,x-1])+int(grid[y,x+1])+int(grid[y,x-1]))
            elif x == length -1:
                #print("right")
                newgrid.append(int(grid[y,x-1]+int(grid[y+1,x-1])+int(grid[y+1,x])+int(grid[y-1,x]+int(grid[y-1,x-1]))))
            else:
                #print("middle")
                newgrid.append(int(grid[y-1,x])+int(grid[y-1,x-1])+int(grid[y-1,x+1])+int(grid[y,x-1])+int(grid[y,x+1])+int(grid[y+1,x])+int(grid[y+1,x+1])+int(grid[y+1,x-1]))
            
        
        else:
            #print(grid[y,x],"coords:",x,y,"mine")
            newgrid.append("X")
        x+=1
        #print("next row")
        
    y+=1
    
newgrid = np.array(newgrid)
newgrid.shape = (length, height)

shownboard[sy,sx] = newgrid[sy,sx]

shownboard[sy-1,sx] = newgrid[sy-1,sx]
shownboard[sy-1,sx+1] = newgrid[sy-1,sx+1] 
shownboard[sy-1,sx-1] = newgrid[sy-1,sx-1] 
shownboard[sy+1,sx-1] = newgrid[sy+1,sx-1] 
shownboard[sy,sx-1] = newgrid[sy,sx-1] 
shownboard[sy+1,sx] = newgrid[sy+1,sx] 
shownboard[sy+1,sx+1] = newgrid[sy+1,sx+1]
shownboard[sy,sx+1] = newgrid[sy,sx+1]
print(shownboard)
def check(x,y):
    if newgrid[y,x] == "X":
        print("game over")
        print(newgrid)
        return False
    else:
        shownboard[y,x] = newgrid[y,x]
        print(shownboard)
        return True

def flag(action,x,y):
    if action == "+":
        shownboard[y,x] = "⛝"
        print(shownboard)
    elif action == "-":
        shownboard[y,x] = "■"
        print(shownboard)

while running:
    x = input("x or flag: ")
    if x == "flag":
        flag(input("add or remove: "), int(input("x: ")), int(input("y: "))) 
    else:
        y = int(input("y: "))
        running = check(int(x),y)
    if "■" not in shownboard:
        print("you win!")
        running = False