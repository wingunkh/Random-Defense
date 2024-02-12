def dfs(x, depth):
    if depth == m:
        print(*result, sep = ' ')
        
        return

    for i in range(x, n+1):
        result.append(i)
        dfs(i+1, depth+1)
        result.pop()

n, m = map(int, input().split())
result = []

dfs(1, 0)
