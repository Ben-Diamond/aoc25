with open(".//aoc//2025//day_02//data.txt") as f:
    data = f.read().split(",")
import numpy as np #maybe

# data=["1-5000"]



def sum(a,b): #sum(1,b) - sum(1,a-1)
    return int( (b/2)*(b+1) - ((a-1)/2)*a )

total = 0
for n in data:
    low, high = n.split("-")

    #if high is 2 digits and low is 4 digits, we want to first do two digits then do 4
    ranges = []
    for l in range(len(low),len(high) +1):
        #we want to add the possible numbers that are l digits long
        if l%2 == 1:
            continue
        
        #if low, high both in range then [low, high]
        if l == len(low):
            bottom = low
        else:
            bottom = "1"+"0"*(l-1)
        if l == len(high):
            top = high
        else:
            top = "9"*l
        
        ranges.append([bottom,top])
    
    if len(ranges) > 1:
        print(ranges)
    
    for low, high in ranges:

        size = len(low)//2

        # smallest invalid id
        small = int(low[:size])
        #if the second half is bigger, skip
        if int(low[size:]) > small: 
            small += 1
        
        #biggest invalid id
        big = int(high[:size])
        #if the second half is smaller, skip
        if int(high[size:]) < big:
            big -= 1

        print(small, big)
        # calculate the sum between smallsmall and bigbig
        multiplier = 10**size + 1 #very true
        total += multiplier * sum(small,big)

print(total)