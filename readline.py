f = open("menus.txt", 'r')
lines = f.readlines()
list = [[], [], []]
for index, line in enumerate(lines):
    line = line.split(",")
    list[0].append(line[0])
    list[1].append(line[1])
    list[2].append(line[2][:-1])
f.close()
print(list)
