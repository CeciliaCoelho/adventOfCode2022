f = open('input4.txt')

data = f.read().strip().split('\n')

data = list(map(lambda x: x.split(','), data))

count = 0
for i in data:
    elf0 = i[0].split('-')
    elf1 = i[1].split('-')

    elf0 = [i for i in range(int(elf0[0]), int(elf0[1])+1)]
    elf1 = [i for i in range(int(elf1[0]), int(elf1[1])+1)]

    if any(list(map(lambda x: x in elf1, elf0))) or any(list(map(lambda x: x in elf0, elf1))): count += 1

print(count)

