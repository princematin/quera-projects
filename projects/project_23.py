from typing import Generator

def divs(n: int) -> Generator[int, None, None]:
    for i in range(n+1):
        if i == 0:
            continue
        if n % i == 0:
            yield i

