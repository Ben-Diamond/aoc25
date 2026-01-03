with open(".//aoc//2025//day_05//data.txt") as f:
    data = f.read().split("\n")


ranges = []
total = 0
setup = True
for line in data:
    if line == "":
        setup = False
        continue
    if setup:
        ranges.append(tuple(map(int,line.split("-"))))

    else:
        id = int(line)

        for low, high in ranges:
            if id >= low and id <= high:
                total += 1
                break

print(ranges)
print(total)