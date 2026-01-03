with open(".//aoc//2025//day_05//data.txt") as f:
    data = f.read().split("\n")

ranges = []
total = 0

for line in data:
    if line == "":
        for r in range(len(ranges)):
            total += ranges[r][1] - ranges[r][0] + 1
        print(ranges)
        print(total)
        break

    
    low, high = map(int,line.split("-"))

    i = 0
    while i < len(ranges):
        if i== len(ranges) or ranges[i][0] > high:
            break
        # 1) overlaps the range completely
        # 2) is overlapped completely
        # 3) overlaps partially from the left
        # 4) overlaps partially from the right
        # 5) we have passed it - insert what remains

        # 5)

        # 1)
        if low <= ranges[i][0] and high > ranges[i][1]:
            ranges[i][0] = low
            low = ranges[i][1] + 1
        # 2)
        elif low >= ranges[i][0] and high <= ranges[i][1]:
            high = low - 1 #do not add
            break
        # 3)
        elif low < ranges[i][0] and high <= ranges[i][1]:
            ranges[i][0] = low
            high = low - 1 #do not add
            break
        # 4)
        elif low > ranges[i][0] and low <= ranges[i][1] and high >= ranges[i][1]:
            low = ranges[i][1] + 1

        i += 1

    if low <= high:
        ranges.insert(i, [low, high])
        #the thing currently at i must have a greater value
