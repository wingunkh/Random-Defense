n = int(input())
a = [[] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

def dfs(start, v):
    for i in a[v]:
        if not visited[start][i]:
            visited[start][i] = 1
            dfs(start, i)

for i in range(n):
    buff = list(map(int, input().split()))

    for j in range(n):
        if buff[j] == 1:
            a[i].append(j)

for i in range(n):
    dfs(i, i)

    print(*visited[i], sep=' ')
