import re


def solve(equation: str) -> str:
    left, c = equation.split("=")
    a, b = left.split("+")

    a = a.strip()
    b = b.strip()
    c = c.strip()

    if "#" in a:
        correct = int(c) - int(b)
        if correct < 0:
            return "-1"
        pattern = "^" + a.replace("#", r"\d*") + "$"
        answer = str(correct)
        if re.fullmatch(pattern, answer):
            return equation.replace(a, answer)
        return "-1"

    elif "#" in b:
        correct = int(c) - int(a)
        if correct < 0:
            return "-1"
        pattern = "^" + b.replace("#", r"\d*") + "$"
        answer = str(correct)
        if re.fullmatch(pattern, answer):
            return equation.replace(b, answer)
        return "-1"

    else:
        correct = int(a) + int(b)
        answer = str(correct)
        pattern = "^" + c.replace("#", r"\d*") + "$"
        if re.fullmatch(pattern, answer):
            return equation.replace(c, answer)
        return "-1"
    
