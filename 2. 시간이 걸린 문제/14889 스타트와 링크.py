import sys

def dfs(x, depth):
    global result
    
    if depth == n // 2:
        start = 0
        link = 0

        for r in range(n):
            for c in range(n):
                if visited[r] and visited[c]:
                    start += a[r][c]
                elif not visited[r] and not visited[c]:
                    link += a[r][c]

        result = min(result, abs(start - link))

        return

    for i in range(x, n):
        visited[i] = True
        dfs(i + 1, depth + 1)
        visited[i] = False


n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [False for _ in range(n)]
result = sys.maxsize

dfs(0, 0)

print(result)
