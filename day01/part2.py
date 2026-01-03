with open(".//aoc//2025//day_01//data.txt") as f:
    data = f.read().split("\n")

total = 0
position = 50
for line in data:
    # left decerases, right increases

    if line[0] == "R":
        position = position + int(line[1:])
        while position >= 100:
#            total += 1
            position -= 100
    elif line[0] == "L":
        if position == 0: #this would have already been counted when previous one landed there
            total -=1
        position = position - int(line[1:])
        while position < 0:
#            total += 1
            position += 100
        if position == 0: #so it is counted to fulfill the above comment. this system is needed otherwise left starting on 0 would double counted
            total += 1


    print(position)

print(total)
#6580 too high