def backtracking(x):
    global result
    
    if sum(stack) == m and stack:
        result += 1
        
    for i in range(x, n):
        stack.append(a[i])
        backtracking(i + 1)
        stack.pop()

n, m = map(int, input().split())
a = list(map(int, input().split()))
stack = []
result = 0

backtracking(0)

print(result)
