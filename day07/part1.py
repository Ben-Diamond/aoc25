with open(".//aoc//2025//day_07//data.txt") as f:
    data = f.read().split("\n")

beams = set()

for x in range(len(data[0])):
    if data[0][x] == "S":
        beams.add((0,x))
        break

#bfs
total = 0
for y in range(1,len(data)):
    new_beams = set()
    for beam in beams:
        x = beam[1]
        if data[y][x] == "^":
            total += 1
            # ^^ never happens
            new_beams.add((y,x-1))
            new_beams.add((y,x+1))
        else:
            new_beams.add((y,x))
    beams = new_beams.copy()

print(total)