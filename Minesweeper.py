import random
import numpy as np

grid = []
nom = 0
for i in range(196):
    x = random.randint(0,6)
    if x == 1:
        grid.append("1")
        nom +=1
    else:
        grid.append("O")
        
        
grid = np.array(grid)
grid.shape = (14, 14)

print(nom)
print(grid)


l =
d =
r =
u =
ul =
ur =
dr =
dl = [y+1,

y = 0
for i in grid:
    x = 0
    for x in i:
        print(x,"sd")