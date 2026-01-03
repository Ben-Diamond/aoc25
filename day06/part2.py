with open(".//aoc//2025//day_06//data.txt") as f:
    data = f.read().split("\n")

# the operator is always on the first digit

xs = []
operators = []
ops = {"*": lambda a,b: a*b,
      "+": lambda a,b: a+b}
id = {"*":1,
      "+":0}

for x in range(len(data[-1])):
    if data[-1][x] != " ":
        operators.append(data[-1][x])
        xs.append(x)
xs.append(len(data[-1]) + 1)

total = 0
for x in range(len(xs) - 1):
    op = operators[x]
    score = id[op]
    start, end = xs[x], xs[x+1]
    for i in range(start, end-1):
        num_string = ""
        for d in [data[l][i] for l in range(len(data)-1)]:
            if d != " ":
                num_string += d
        score = ops[op](score, int(num_string))

    print("score", score)

    total += score

print(total)
