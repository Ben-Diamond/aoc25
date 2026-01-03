with open(".//aoc//2025//day_02//data.txt") as f:
    data = f.read().split(",")
import numpy as np #maybe


total = 0

ranges = []
used = set()

for n in data:
    low, high = n.split("-")
    #len(high) - len(low) <= 1
    if len(low) == len(high):
        ranges.append((low,high))
    else:
        ranges.append((low, "9"*len(low)))
        ranges.append(("1"+"0"*(len(high)-1),high))
print(ranges)
for low, high in ranges:
    for t in range(1,1+len(low)//2):
        #t is the size of the number
        if len(low) % t != 0:
            continue

        repetitions = len(low)//t
        number = low[:t]
        while int(number*repetitions) < int(low):
            number = str(int(number) + 1)
        while int(number*repetitions) <= int(high) and len(number) == t:
            print(int(number*repetitions),low,high)
            if number*repetitions not in used:
                total += int(number*repetitions)
            used.add(number*repetitions)
            
            number = str(int(number) + 1)
            
        

print(total)