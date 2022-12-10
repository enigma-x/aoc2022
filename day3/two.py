file1 = open('input/input', 'r')

def getGroupDupe(data):
    dupes = []
    for x in data[0]:
        if x in data[1]:
            if x in data[2]:
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
group = []
groupDupes = []
while a:
    line = file1.readline()
    if line:
        if len(group) < 3:
            group.append(line.strip())
        else:
            groupDupes.append(getGroupDupe(group))
            group = []
            group.append(line.strip())
    if not line:
        groupDupes.append(getGroupDupe(group))
        a = False
file1.close()

#print(groupDupes)
print(getScore(groupDupes))