with open(".//aoc//2025//day_04//data.txt") as f:
    data = f.read().split("\n")


papers = set() #x,y
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "@":
            papers.add((x,y))

total = 0
for x,y in papers:
    surrounding = 0
    for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
        if (x+dx,y+dy) in papers:
            surrounding += 1
    if surrounding < 4:
        total += 1

print(total)