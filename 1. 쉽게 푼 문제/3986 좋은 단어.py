n = int(input())
result = 0

for _ in range(n):
    s = list(input())
    stack = []

    for i in s:
        if not stack:
            stack.append(i)
        else:
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)

    if not stack:
        result += 1

print(result)
