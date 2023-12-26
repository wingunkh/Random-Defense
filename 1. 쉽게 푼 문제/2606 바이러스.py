def dfs(v):
    global result
    
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            result += 1
            dfs(i)

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
result = 0

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

dfs(1)

print(result)
