file1 = open('input/input', 'r')

def getScore(data):
    x = data.split()
    score1 = winScore(x)
    score2 = playScore(x,score1)
    total = score1 + score2
    return total

def winScore(data):
    if data[1] == 'Y':
        return 3
    elif data[1] == 'Z':
        return 6
    else:
        return 0

def playScore(data1,data2):
    if data2 == 0:
        if data1[0] == 'A':
            return 3
        if data1[0] == 'B':
            return 1
        if data1[0] == 'C':
            return 2
    
    if data2 == 3:
        if data1[0] == 'A':
            return 1
        if data1[0] == 'B':
            return 2
        if data1[0] == 'C':
            return 3

    if data2 == 6:
        if data1[0] == 'A':
            return 2
        if data1[0] == 'B':
            return 3
        if data1[0] == 'C':
            return 1

a = True
totalscore = 0
while a:
    line = file1.readline()
    if line:
        totalscore = totalscore + getScore(line)
    if not line:
        a = False

file1.close()
print(totalscore)
