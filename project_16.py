stack = []

menu = input()

for item in menu:
    if item == '=':
        if stack:
            stack.pop()
    else :
        stack.append(item)

stack = ''.join(stack)

print(stack)