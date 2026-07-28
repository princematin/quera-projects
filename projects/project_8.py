import math

x = int(input())
r = math.radians(x)

a = math.ceil(math.pow(x, 5/3) + math.tan(r))
b = math.floor(math.pow(math.pi, 2 + math.atan(math.sin(r) ** 2)))


print(math.gcd(a, b))
