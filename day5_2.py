import itertools

f = open('input5.txt')

data = f.read().strip().split('\n\n')

#stacks = list(map(lambda x: x.split(' '),data[0].split('\n')))[:-1]

l = [list(reversed( ['J', 'Z', 'G', 'V', 'T', 'D', 'B', 'N'])), list(reversed( ['F', 'P', 'W', 'D', 'M', 'R', 'S'])),list(reversed( ['Z', 'S', 'R', 'C', 'V'])),list(reversed( ['G', 'H', 'P', 'Z','J','T','R'])),list(reversed( ['F','Q','Z','D','N','J','C','T'])),list(reversed( ['M','F','S','G','W','P','V','N'])),list(reversed( ['Q','P','B','V','C','G'])),list(reversed( ['N','P','B','Z'])),list(reversed( ['J','P','W']))]


moves = data[1].strip().split('\n')
moves = list(map(lambda x: x.split(' '), moves))


s = 0
for i in moves:
    l[int(i[5])-1].extend(list((l[int(i[3])-1][-int(i[1]):])))
    l[int(i[3])-1][-int(i[1]):] = '' 

print(l)


