import sys
input = sys.stdin.readline

def dfs(x, sum, depth):
    global result
    
    if depth == n - 1:
        if a[x][1] > 0:
            result = min(result, sum + a[x][1])
        
        return

    for i in range(2, n + 1):
        if not visited[i] and a[x][i] > 0:
            visited[i] = True
            dfs(i, sum + a[x][i], depth + 1)
            visited[i] = False
        
n = int(input())
a = [[0 for _ in range(n + 1)]]
visited = [False for _ in range(n + 1)]
result = sys.maxsize

for _ in range(n):
    buff = list(map(int, input().split()))
    a.append([0] + buff)

dfs(1, 0, 0)

print(result)
