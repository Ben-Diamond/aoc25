with open(".//aoc//2025//day_04//data.txt") as f:
    data = f.read().split("\n")

#straightforward ?

papers = set() #x,y
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == "@":
            papers.add((x,y))

total = 0
while True:
    removing = set()
    for x,y in papers:
        surrounding = 0
        for dx, dy in ((-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)):
            if (x+dx,y+dy) in papers:
                surrounding += 1
        if surrounding < 4:
            total += 1
            removing.add((x,y))

    if len(removing) == 0:
        print(total)
        exit()

    papers = papers - removing #how delightfully simple
    print(total)

