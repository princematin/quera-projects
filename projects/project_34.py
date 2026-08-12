import re


def real_numbers(numbers: list[str]) -> list[str]:
    anss = list()
    for item in numbers:
        if re.search(r"^\s*[+-]?(\d+(\.\d+)?)([eE][+-]?\d+)?\s*$", item):
            anss.append('LEGAL')
        else:
            anss.append('ILLEGAL')
    return anss

