with open(".//aoc//2025//day_01//data.txt") as f:
    data = f.read().split("\n")

total = 0
position = 50
for line in data:
    # left decerases, right increases

    if line[0] == "R":
        position = (position + int(line[1:])) % 100
    elif line[0] == "L":
        position = (position - int(line[1:])) % 100
    if position == 0:
        total += 1
    print(position)

print(total)
