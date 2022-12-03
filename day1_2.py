f = open('input1.txt')

data = f.read().split('\n\n')

data = list(map(lambda x: x.strip().split('\n'), data))

maxElves = [0]*len(data)
for i in range(len(data)):
    tot = 0
    for j in data[i]:
        tot += int(j.strip("'"))
        maxElves[i] = tot

maxElves = sorted(maxElves)[-3:]

print(sum(maxElves))
