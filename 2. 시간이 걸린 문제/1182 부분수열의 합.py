def dfs(x):
    global result
    
    if stack and sum(stack) == m:
        result += 1

    if x == n:
        return

    for i in range(x, n):
        stack.append(a[i])
        dfs(i + 1)
        stack.pop()

n, m = map(int, input().split())
a = list(map(int, input().split()))
stack = []
result = 0

dfs(0)

print(result)
