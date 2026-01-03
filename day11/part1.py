with open(".//aoc//2025//day_11//data.txt") as f:
    data = f.read().split("\n")


# number of paths from "you" until "out"
# bfs ?

devices = {}
numpaths = {"you":1}

for line in data:
    device = line.split(":")[0]
    output = line.split(" ")[1:]
    if device in devices:
        print("what")
    devices[device] = set(output)
print(devices)


# no such thing as a "slow path" -- this is a tree-like structure

queue = set()
queue.add("you")
t=0
while len(queue) > 0:
    newq = set()
    t += 1
    for device in queue:
        for out in devices[device]:            
            if out not in numpaths:
                numpaths[out] = 0
            numpaths[out] += numpaths[device]
                
            if out == "out":
                # print("(end)")
                continue

            newq.add(out)

    print(len(newq))

    queue = newq.copy()

print(numpaths, numpaths["out"])