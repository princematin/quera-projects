
def calc(lst: list) -> tuple:
    avrage = sum(lst) / len(lst)
    median = sorted(lst)
    median_len = len(median)
    if median_len % 2 == 1:
        median = median[median_len // 2]
    else :
        median = (median[median_len // 2 - 1] + median[median_len // 2]) / 2
    max_num = max(sorted(lst))

    return (avrage, median, max_num)

