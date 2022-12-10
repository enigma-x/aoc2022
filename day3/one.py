file1 = open('input/input', 'r')

def splitItems(data):
    x = []
    x.append(data[:len(data)//2])
    x.append(data[len(data)//2:])
    return(x)

def getDupe(data):
    dupes = []
    for x in data[0]:
        if x in data[1]:
            if x not in dupes:
                dupes.append(x)
    return(dupes)

def getScore(data):
    score = 0
    for x in data:
        if x[0].islower():
            score = score + (ord(x[0])-96)
        else:
            score = score + (ord(x[0])-38)
    return(score)

a = True
dupes = []
while a:
    line = file1.readline()
    if line:
        dupes.append(getDupe(splitItems(line.strip())))
    if not line:
        a = False
file1.close()

print(getScore(dupes))