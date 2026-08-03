import json

door = int(input())
ns = []
for _ in range(door):
    n = input()
    ns.append(n)

variables = dict()

for item in ns:
    if ":=" in item:
        line = item.split(" := ")
        variables[line[0]] = json.loads(line[1])
    else:
        line = item.replace("print ", "")
        line = line.replace("]", "")
        line = line.split("[")
        line[1] = json.loads(line[1])
        
        javab = variables[line[0]][line[1]]
        print(javab)