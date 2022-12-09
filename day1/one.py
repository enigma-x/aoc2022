file1 = open('resources/input', 'r')

elfs = []  
calories = 0
a = True

while a:
    line = file1.readline()
    if line:
        if (line.strip()).isnumeric():
            calories = int(calories) + int(line)
        
        else:
            elfs.append(calories)
            calories  = 0

    if not line:
        elfs.append(calories)
        a = False
file1.close()

print(max(elfs))  

    
