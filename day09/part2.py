with open(".//aoc//2025//day_09//data.txt") as f:
    data = f.read().split("\n")
import numpy as np

# a rectangle is invalid iff there is a point on one of its sides that's not greens

#for each side, we want a direction that points inside the shape - assume no overlap, so this is just the direction to neighbouring sides



directions = {}


#we only need to consider co-ordinates where a reds tile lies
#make things x,y
xs = set()
ys = set()

#the tiles ARE in order - one of the co-ordinates will match with the next line
for l,line in enumerate(data):
    tile1 = tuple(map(int, line.split(",")))

    tile2 = tuple(map(int,data[(l+1)%len(data)].split(",")))
    
    dir = np.sign(np.array(tile2)- np.array(tile1))
    xs.add(int(tile1[0]))
    ys.add(int(tile1[1]))

    if tile1 not in directions:
        directions[tile1] = []
    directions[tile1].append(dir)

    if tile2 not in directions:
        directions[tile2] = []
    directions[tile2].append(-dir)
    
print(directions)
#across, down

#494 of each
#no two walls are right next to each other
xmap = {}
ymap = {}
xs = sorted(list(xs))
ys = sorted(list(ys))
# condense the problem!!! try without gaps first
# print(len(coords))


#first add the points between edges


for x in range(len(xs)):
    xmap[xs[x]] = x
for y in range(len(ys)):
    ymap[ys[y]] = y

print(xmap)
print(ymap)


reds = set()
greens = set()
for l, line in enumerate(data):
    
    tile1 = tuple(map(int, line.split(",")))
    tile2 = tuple(map(int,data[(l+1)%len(data)].split(",")))

    left = 0

    dx, dy = map(int,np.sign(np.array(tile2)- np.array(tile1)))

    x = xmap[tile1[0]]
    y = ymap[tile1[1]]

    reds.add((x,y))

    while True:
        x,y = x+dx, y+dy
        greens.add((x,y))
        if (xs[x],ys[y]) in directions: #this is a red tile
            break

#

# reds, greens are in transformed space
# xs[x] takes us to real space (replacing coords)
# xmap[x] takes us to transformed space


print(greens)
print(len(greens))
print(reds)


queue = []
for x,y in reds:
    # queue.append((x + 2,y + 0))  #for example
    queue.append((x - 1,y - 1))
    break
#to find first tile

#GUESS first direction - is either inside or outside
if queue[0] in greens:
    print("THIS DOES NOT WORK!")
    exit()

inside = set(queue)
#in transformed space forever

while len(queue) > 0:
    newq = []
    
    for x,y in queue:
        for dx,dy in ((0,1),(0,-1),(1,0),(-1,0)): #, (1,1), (1,-1), (-1,1), (-1,-1)):
            pos = (x+dx,y+dy)
            
            if pos in greens:
                # print("yeah it's in greens")
                continue
            
            if pos not in inside:
                inside.add(pos) #yeah i know
                newq.append(pos)


    queue = newq.copy()
    # print("queue length:",len(queue), "inside:",len(inside))
# print(inside)
print(len(inside))

inside = inside.union(greens)
inside = inside.union(reds)
def draw():
    #transformed space
    out=""
    for y in range(len(ys)):
        out += "\n"
        for x in range(len(xs)):
            if (x,y) in inside:
                out += "#"
            else:
                out+="."
    with open(".//aoc//2025//day_09//drawing.txt","w") as f:
        f.write(out)
        f.close()

print(len(xmap))
print(len(ymap))
# draw()
# print(inside)

#fro biden in transformed space if fro biden in normal space

biggest = 0
for tile1 in reds:
    for tile2 in reds:
        #check forbidden
        x1, y1 = tile1
        x2, y2 = tile2
        if x1 == x2 and y1 == y2:
            continue
        #go along the border - if one tile isn't allowed then remove it 

        #horizontal sides
        directionx = 1 if x2>x1 else -1
        allowed = True
        x = x1
        while x != x2:
            
            if ((x,y1) not in inside) or ((x,y2) not in inside):
                allowed = False
                break
            x += directionx
        if not allowed: 
            continue

        directiony = 1 if y2>y1 else -1
        y = y1
        while y != y2:
            if ((x1,y) not in inside) or ((x2,y) not in inside):
                allowed = False
                break
            y += directiony
        if not allowed: 
            continue


        area = (1+abs(xs[x1]-xs[x2])) * (1+abs(+ys[y1]-ys[y2]))
        if area > biggest:
            biggest = area

print(biggest)
