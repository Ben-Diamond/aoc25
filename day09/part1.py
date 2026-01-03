with open(".//aoc//2025//day_09//data.txt") as f:
    data = f.read().split("\n")

# we want the largest rectangle
largest = 0

for line in data:
    tile1 = [int(x) for x in line.split(",")]
    for line2 in data:
        tile2 = [int(x) for x in line2.split(",")]
        area = abs( (1+tile1[0]-tile2[0]) * (1+tile1[1]-tile2[1]))
        if area > largest:
            largest = area
print(largest)