with open(".//aoc//2025//day_10//data.txt") as f:
    data = f.read().split("\n")
import numpy as np
from math import comb
# goal is to get the lights corresponding to [.##.] turned on
# button has a list of things it toggles

print(data[0])

total = 0

def increment(state_array):
    #find the first 0, turn it into a 1 and flip everything before it
    i = 0
    while state_array[i] == 1:
        state_array[i] = 0
        i += 1
    state_array[i] = 1

    return state_array

# s = np.zeros(4)
# for x in range(15):
#     s = increment(s)
#     print(s)

# exit()

total = 0
for line in data:
    goal = np.array([0 if l == "." else 1 for l in line.split(" ")[0][1:-1]])
    buttons = np.array([[1 if l in tuple(int(x) for x in b[1:-1].split(",")) else 0 for l in range(len(goal))] for b in line.split(" ")[1:-1]]) #i am a genius
    numb = len(buttons)
    """ 
    never need to press a button more than once because it's binary
    just try every combination
    """

    #every possible combination is "just" n! of them
    states = np.zeros(numb)
    # while len(queue)
    lowest = 10000
    #not efficient
    for l in range(2**numb-1):
        lights = np.mod(states.T @ buttons,2)
        

        if (lights == goal).all():
            # we gound it
            if np.sum(states) < lowest:
                lowest = np.sum(states)
            

        states = increment(states)
    total += lowest

print(total)
