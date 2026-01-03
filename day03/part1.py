with open(".//aoc//2025//day_03//data.txt") as f:
    data = f.read().split("\n")


#more efficient than the easiest way! o(n) per line

total = 0
for line in data:
    batteries = [int(x) for x in line]

    largest = -1
    largest_idx = -1

    for b in range(len(batteries)-1): #don't try the last one because it can't be the first digit
        if batteries[b] > largest: #with >, we get the first one
            largest = batteries[b]
            largest_idx = b

    second_largest = -1
    second_largest_idx = -1
    for b in range(largest_idx + 1, len(batteries)):
        if batteries[b] > second_largest:
            second_largest = batteries[b]
            second_largest_idx = b

    total += largest*10 + second_largest

print(total)