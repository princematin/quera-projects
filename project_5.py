p, d = input().split()
p = int(p)
d = int(d)
i = 1
while True :
    mazrab = i * d
    baghi = mazrab % p
    if 0 <= baghi <= (p // 2) :
        print(mazrab)
        break

    i += 1