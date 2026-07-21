nums = []
while True :
    menu = int(input())
    if menu == 0 :
        break
    else :
        nums.append(menu)

nums.reverse()
for i in nums:
    print(i)