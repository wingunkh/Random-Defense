from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q:
        x, time = q.popleft()

        if x == m:
            return time

        for i in (x - 1, x + 1, 2 * x):
            if 0 <= i <= 100000 and not visited[i]:
                q.append((i, time + 1))
                visited[i] = True

n, m = map(int, input().split())
visited = [False for _ in range(100001)]

print(bfs(n))
