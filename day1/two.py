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

sort = elfs.sort(reverse=True)

sum = 0
for i in range(3):
    sum = sum + elfs[i]

print(sum)



    
