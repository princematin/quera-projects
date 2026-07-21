# numbers = list(map(int, input().split()))
# result = []

# for i, j in enumerate(numbers, start=1):
#     if i % 6 == 0 and j % 6 == 0:
#         result.append(j)

# print(*sorted(result))

print(*sorted(num for i, num in enumerate(map(int, input().split()), 1) if i % 6 == num % 6 == 0))

