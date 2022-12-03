f = open('input2.txt')
data = f.read().strip().split('\n')
data = list(map(lambda x: x.split(' '), data))


dicWin = {'A':'B', 'B':'C', 'C':'A'}
dicLose = {'A':'C', 'B':'A', 'C':'B'}
dicSelected = {'A': 1,'B':2, 'C':3}

score = 0

for i in data:
    sel = i[1]
    if sel == 'X':
        score += dicSelected[dicLose[i[0]]]
    elif sel == 'Z':
        score += (dicSelected[dicWin[i[0]]] + 6)
    else:
        score += (dicSelected[i[0]] + 3)


print(score)
