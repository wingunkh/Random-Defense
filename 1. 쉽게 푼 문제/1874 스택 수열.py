n = int(input())
stack = []
count = 0
result = []

for _ in range(n):
    target = int(input())

    while count < target:
        count += 1
        stack.append(count)
        result.append('+')

    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        print("NO")
        break
else:
    print(*result, sep = '\n')
