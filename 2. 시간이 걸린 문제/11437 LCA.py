import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append(1)
    visited[1] = True

    while q:
        now = q.popleft()

        for next in a[now]:
            if not visited[next]:
                q.append(next)
                visited[next] = True
                depth[next] = depth[now] + 1
                parent[next] = now

def lca(x, y):
    while depth[x] > depth[y]:
        x = parent[x]

    while depth[y] > depth[x]:
        y = parent[y]

    while x != y:
        x = parent[x]
        y = parent[y]

    return x
            
n = int(input())
a = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
depth = [0 for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

bfs()

m = int(input())

for _ in range(m):
    x, y = map(int, input().split())
    print(lca(x, y))
