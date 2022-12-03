f = open('input3.txt')

data = f.read().strip().split('\n')

score = 0
for i in data:
    r1 = i[:int(len(i)/2)]
    r2 = i[int(len(i)/2):]

    r1 = list(set(r1))
    r2 = list(set(r2))

    for j in r1:
        if j in r2:
            if j.isupper(): 
                score += (ord(j.lower())-96+26)
            else:
                score += (ord(j)-96)

print(score)
