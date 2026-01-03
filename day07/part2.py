with open(".//aoc//2025//day_07//data.txt") as f:
    data = f.read().split("\n")

beams = {} # y,x : timelines

for x in range(len(data[0])):
    if data[0][x] == "S":
        beams[(0,x)] = 1
        break

#bfs
total = 0
for y in range(1,len(data)):
    new_beams = {}
    for beam in beams:
        x = beam[1]
        timelines = beams[beam]
        if data[y][x] == "^":
            total += 1
            # ^^ never happens
            if (y, x-1) not in new_beams:
                new_beams[(y, x-1)] = 0
            new_beams[(y, x-1)] += timelines

            if (y, x+1) not in new_beams:
                new_beams[(y, x+1)] = 0
            new_beams[(y, x+1)] += timelines

        else:
            if (y,x) not in new_beams:
                new_beams[(y,x)] = 0
            new_beams[(y,x)] += timelines
    beams = new_beams.copy()

print(sum([beams[b] for b in beams]))