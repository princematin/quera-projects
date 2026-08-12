
def capitalize(names: list[str]) -> list[str]:
    names_plus = list()
    for item in names:
        name = item.title()
        names_plus.append(name)
    return names_plus

