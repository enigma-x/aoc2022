file1 = open('input/input', 'r')

def getScore(data):
    x = data.split()
    score1 = winScore(x)
    score2 = playScore(x)
    total = score1 + score2
    return total

def winScore(data):
    win = False
    draw = False
    if (data[0] == 'A' and data[1] == 'Y') or (data[0] == 'B' and data[1] == 'Z') or (data[0] == 'C' and data[1] == 'X'):
        win = True
    
    if (data[0] == 'A' and data[1] == 'X') or (data[0] == 'B' and data[1] == 'Y') or (data[0] == 'C' and data[1] == 'Z'):
        draw = True
    
    if win == True:
        return 6
    elif draw == True:
        return 3
    else:
        return 0

def playScore(data):
    if data[1] == "X":
        score = 1
    if data[1] == "Y":
        score = 2
    if data[1] == "Z":
        score = 3
    return score
    

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
