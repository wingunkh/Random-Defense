n, m = map(int, input().split())
a = [[] for _ in range(n)]

def dfs(v, depth):
    if depth == 4:
        print(1)
        exit()

    for i in a[v]:
        if not visited[i]:
            visited[i] = True
            dfs(i, depth + 1)
            visited[i] = False
    
for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    visited = [False for _ in range(n)]
    visited[i] = True
    dfs(i, 0)
else:
    print(0)
