s = input()
target = list(input())
stack = []

for i in s:
    stack.append(i)
    
    if stack[-len(target):] == target:
        for _ in range(len(target)):
            stack.pop()

if stack:
    print(*stack, sep = '')
else:
    print("FRULA")
