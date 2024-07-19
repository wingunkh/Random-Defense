import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    global count
    
    count += 1
    visited[v] = count
    
    for i in a[v]:
        if not visited[i]:
            dfs(i)

n, m, r = map(int, input().split())
a = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
tmp  = []
count = 0

for _ in range(m):
    s, e = map(int, input().split())
    tmp.append((s, e))

tmp.sort(key = lambda x: (x[0], x[1]))

for s, e in tmp:
    a[s].append(e)
    a[e].append(s)

dfs(r)

for i in range(1, n + 1):
    print(visited[i])
