with open(".//aoc//2025//day_03//data.txt") as f:
    data = f.read().split("\n")

# it paid off

total = 0
for line in data:
    batteries = [int(x) for x in line]
    largest_numbers = [-1 for x in range(12)]
    largest_idxs = [-1 for x in range(12)]

    for l in range(12):
        for b in range(largest_idxs[l-1] + 1,len(batteries)-(11-l)): #don't try the last one because it can't be the first digit
            if batteries[b] > largest_numbers[l]: #witg >, we get the first one
                largest_numbers[l] = batteries[b]
                largest_idxs[l] = b

    total += int("".join(map(str,largest_numbers)))

print(total)