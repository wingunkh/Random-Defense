def dfs(x, depth):
    prev = 0
    
    if depth == m:
        print(' '.join(map(str, result)))

        return

    for i in range(n):
        if not visited[i] and a[i] != prev:
            prev = a[i]
            visited[i] = True
            result.append(a[i])
            dfs(i + 1, depth + 1)
            visited[i] = False
            result.pop()

n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
visited = [False for _ in range(n)]
result = []

dfs(0, 0)
