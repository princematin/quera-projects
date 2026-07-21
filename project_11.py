ghofl_nums = int(input())
ghofl = input()
ghofl_index = 0
for i in range(ghofl_nums):
    charkh_num = (input())
    index = charkh_num.find(ghofl[i])
    ghofl_index += min(index, len(charkh_num) - index)
print(ghofl_index)