f = open('input1.txt')

data = f.read().split('\n\n')

data = list(map(lambda x: x.strip().split('\n'), data))

maxElf = 0
for i in data:
    tot = 0
    for j in i:
        tot += int(j.strip("'"))
    if tot > maxElf: maxElf = tot
        
print(maxElf)
