def dfs(x, depth):
    if depth == m:
        print(*result, sep = ' ')
        
        return

    for i in range(x+1, n+1):
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(i, depth+1)
            visited[i] = False
            result.pop()

n, m = map(int, input().split())
visited = [False for _ in range(n+1)]
result = []

dfs(0, 0)
