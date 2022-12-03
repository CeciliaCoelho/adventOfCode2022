f = open('input3.txt')

data = f.read().strip().split('\n')

score = 0
for i in range(0,len(data),3):

    for j in data[i+0]:
        if j in data[i+1] and j in data[i+2]:
            print(j)
            if j.isupper(): 
                score += (ord(j.lower())-96+26)
            else:
                score += (ord(j)-96)
            break

print(score)
