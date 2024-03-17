import sys
from collections import deque
input = sys.stdin.readline

def bfs(v):
    q = deque()
    q.append((v, 0))
    visited[v] = True

    while q:
        now_v, now_distance = q.popleft()

        if now_distance == k:
            result.append(now_v)
        
        for i in a[now_v]:
            if not visited[i]:
                q.append((i, now_distance + 1))
                visited[i] = True

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
result = []

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

bfs(x)

if result:
    print(*sorted(result), sep = "\n")
else:
    print(-1)
