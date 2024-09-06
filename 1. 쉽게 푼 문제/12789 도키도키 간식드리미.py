n = int(input())
a = list(map(int, input().split()))
stack = []
target = 1

for i in range(n):
    stack.append(a[i])
    
    while stack and stack[-1] == target:
        stack.pop()
        target += 1

if stack:
    print("Sad")
else:
    print("Nice")
