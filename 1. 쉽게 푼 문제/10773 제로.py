n = int(input())
stack = []

for _ in range(n):
    buff = int(input())

    if buff:
        stack.append(buff)
    else:
        stack.pop()

print(sum(stack))
