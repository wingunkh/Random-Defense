import sys

def dfs(x, start, sum, depth):
    global result
    
    if depth == n:
        if a[x][start] > 0:
            result = min(result, sum + a[x][start])
        
        return

    for i in range(1, n + 1):
        if not visited[i] and a[x][i] > 0:
            visited[i] = True
            dfs(i, start, sum + a[x][i], depth + 1)
            visited[i] = False
        
n = int(input())
a = [[0 for _ in range(n + 1)]]
visited = [False for _ in range(n + 1)]
result = sys.maxsize

for _ in range(n):
    buff = list(map(int, input().split()))
    a.append([0] + buff)

for i in range(1, n + 1):
    visited[i] = True
    dfs(i, i, 0, 1)
    visited[i] = False

print(result)
