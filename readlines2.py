f = open("menus.txt", 'r')
lines = f.readlines()
menus = []
for index, line in enumerate(lines[1:]):
    line = line.split(",")
    menu = {}
    menu['key'] = line[0]
    menu['menu'] = line[1]
    menu['price'] = line[2]
    menu['url'] = line[3][:-1]
    menus.append(menu)

f.close()
print(menus)
