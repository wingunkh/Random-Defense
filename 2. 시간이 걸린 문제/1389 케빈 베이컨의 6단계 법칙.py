from collections import deque

n, m = map(int, input().split())
a = [[] for _ in range(n+1)]
result = [0 for _ in range(n+1)]

def bfs(v, depth):
    global result
    
    q = deque()        
    q.append((v, depth))
    visited[v] = True

    while q:
        now_node, now_depth = q.popleft()
        result[v] += now_depth

        for i in a[now_node]:
            if not visited[i]:
                q.append((i, now_depth + 1))
                visited[i] = True

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(1, n+1):
    visited = [False for _ in range(n+1)]
    bfs(i, 0)

print(result.index(min(result[1:])))
