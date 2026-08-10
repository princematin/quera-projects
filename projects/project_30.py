def calculator(n: int, m: int, ls: list[int]) -> int:
    jam_adad = list()
    i = 0
    for _ in range(n):
        list_add = sum(ls[i : i+m])
        if not list_add:
            continue
        jam_adad.append(list_add)
        i = i + m
    final_ans = 0
    for index, item in enumerate(jam_adad):
        if index % 2 == 0:
            final_ans += item
        else:
            final_ans -= item
    return final_ans
