f = open('input2.txt')
data = f.read().strip().split('\n')
data = list(map(lambda x: x.split(' '), data))


dicWin = {'A':'Y', 'B':'Z', 'C':'X'}
dicDraw = {'A':'X', 'B':'Y', 'C':'Z'}
dicSelected = {'X': 1,'Y':2, 'Z':3}

score = 0

for i in data:
    score += dicSelected[i[1]]

    if dicWin[i[0]] == i[1]: 
        score += 6
    elif dicDraw[i[0]] == i[1]: 
        score += 3


print(score)
