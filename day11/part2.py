with open(".//aoc//2025//day_11//data.txt") as f:
    data = f.read().split("\n")


# number of paths from "you" until "out"
# bfs ?

devices = {}
done = set()
max_times = {}

for line in data:
    device = line.split(":")[0]
    output = line.split(" ")[1:]
    if device in devices:
        print("what")
    devices[device] = set(output)
print(devices)


# no such thing as a "slow path" -- this is a tree-like structure
# this is no longer true for the other sections, but iss
# this does not actually work. need to think


# svr -> fft
# fft -> dac
# dac -> out
queue = set()
queue.add("svr")

t=0
# svr -> fft; number of paths
while len(queue) > 0:
    newq = set()
    t += 1
    for device in queue:
        for out in devices[device]:
            if out == "out":
                continue
            max_times[out] = t
            newq.add(out)

    queue = newq.copy()
#they're up to 37

max_t = t
max_times["out"] = max_t 
future_queues = [set() for x in range(max_t+2)]

t=0
checkpoints = ["svr","fft","dac","out"]
# checpo

c=0
numpaths = {checkpoints[c]:1}
queue = set()
queue.add(checkpoints[c])
print(max_times)
while len(queue) > 0:
    
    t += 1
    newq = future_queues[t].copy()

    for device in queue:
        for out in devices[device]:
            
            if out not in numpaths:
                numpaths[out] = 0
            # print(device, queue, out)
            numpaths[out] += numpaths[device]
            if max_times[out] > t:
                future_queues[max_times[out]].add(out)
            elif out != "out":
                newq.add(out)
                  
    if t-1 == max_times[checkpoints[c+1]]:
        print(t, queue, newq)
        # next phase
        c += 1

        print(f"There are {numpaths[checkpoints[c]]} paths for {checkpoints[c]}, time {t}")
        if c == 3:
            print("we won", checkpoints[c], numpaths[checkpoints[c]])
            exit()
        future_queues = [set() for x in range(max_t+2)]
        numpaths = {checkpoints[c]: numpaths[checkpoints[c]]}
        queue = set()
        queue.add(checkpoints[c])
    
    else:  
        queue = newq.copy()

print(numpaths)