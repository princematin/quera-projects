name_count = int(input())
nums = []
for i in range(name_count):
    name = input()
    nums.append(len(set(name)))

bishtarin_motemayez = max(nums)
print(bishtarin_motemayez)