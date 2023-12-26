def dfs(x, sum, depth):
    global result

    if depth == 3:
        if sum <= m:
            result = max(result, sum)

        return

    for i in range(x, n):
        if not visited[i]:
            visited[i] = True
            dfs(i+1, sum + a[i] , depth+1)
            visited[i] = False
    
n, m = map(int, input().split())
a = list(map(int, input().split()))
visited = [False for _ in range(n)]
result = 0

dfs(0, 0, 0)

print(result)
