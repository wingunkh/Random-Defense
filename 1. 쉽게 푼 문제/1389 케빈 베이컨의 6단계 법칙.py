from collections import deque

def bfs(v):
    global result
    
    q = deque()
    q.append((v, 0))
    visited[v] = True

    while q:
        now_node, depth = q.popleft()
        result[v] += depth

        for i in a[now_node]:
            if not visited[i]:
                q.append((i, depth + 1))
                visited[i] = True
    
n, m = (map(int, input().split()))
a = [[] for _ in range(n + 1)]
result = [0 for _ in range(n + 1)]

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(1, n + 1):
    visited = [False for _ in range(n + 1)]
    bfs(i)

print(result.index(min(result[1:])))
