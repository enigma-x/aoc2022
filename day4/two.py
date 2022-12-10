file1 = open('input/input', 'r')

def checkOverlap(data):
    x = data.split(',')
    set1 = x[0].split('-')
    set2 = x[1].split('-')

    if (int(set1[0]) >= int(set2[0])) and (int(set1[1]) <= int(set2[1])):
        return True
    
    elif (int(set1[0]) <= int(set2[0])) and (int(set1[1]) >= int(set2[1])):
        return True

    elif (int(set1[0]) <= int(set2[0])) and (int(set1[1]) <= int(set2[1])) and (int(set1[1]) >= int(set2[0])):
        return True
    
    elif (int(set2[0]) <= int(set1[0])) and (int(set2[1]) <= int(set1[1])) and (int(set2[1]) >= int(set1[0])):
        return True
    
    else:
        return False
   
a = True
count = 0
while a:
    line = file1.readline()
    if line:
        if checkOverlap(line.strip()) is True:
            count += 1
    if not line:
        a = False
file1.close()

print(count)
