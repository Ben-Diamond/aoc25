with open(".//aoc//2025//day_08//data.txt") as f:
    data = f.read().split("\n")
import numpy as np

distances = []
done = set()

circuits = [] #list of sets
connections = {}

for box1 in data:
    done.add(box1)
    for box2 in data:
        if box2 in done:
            continue

        vec1 = np.array(box1.split(","), int)
        vec2 = np.array(box2.split(","), int)
        # vec2 = [int(x) for x in box2.split(",")]
        distances.append((np.linalg.norm(vec2-vec1),box1,box2))
        # distances[box1][box2] = np.linalg.norm(vec2-vec1)
print("Done collecting")
distances.sort()
print("Done sorting")

# a = set()
# a.add(1)

# c=set()
# c.add(2)

# b=set()
# b.add(3)
# print(a.union(b,c))

# exit()
con = 0
while True:
    box1, box2 = distances[con][1:]
    
    circuitsIn = []
    for c,circuit in enumerate(circuits):
        if box1 in circuit or box2 in circuit:
            circuitsIn.append(c)

    if len(circuitsIn) == 0:
        circuits.append(set((box1,box2)))
    elif len(circuitsIn) == 1:
        circuits[circuitsIn[0]].add(box1)
        circuits[circuitsIn[0]].add(box2)
    else:
        temp = circuits[circuitsIn[0]]
        for num in range(1,len(circuitsIn)):
            temp = temp.union(circuits[circuitsIn[num]])
        circuits.append(temp)

        circuits = [circuits[e] for e in range(len(circuits)) if e not in circuitsIn] #they are now encompassed in the new circuits

    if len(circuits) == 1 and len(circuits[0]) == len(data):
        print(len(circuits[0]))
        print(f"Done! on the {con}th connection")
        print(int(box1.split(",")[0])*int(box2.split(",")[0]))
        break

    con += 1
