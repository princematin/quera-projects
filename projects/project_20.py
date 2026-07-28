names = []

rounds = int(input())

for i in range(rounds):
    
    names.append(input())

names_split = [person.split()[0] for person in names]

tedad_name_count = []

for item in names_split:
    tedad_name_count.append(names_split.count(item))

tedad_kolah = max(tedad_name_count)

print(tedad_kolah)