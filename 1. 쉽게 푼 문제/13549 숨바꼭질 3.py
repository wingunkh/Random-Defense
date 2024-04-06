from collections import deque

def bfs(x, time):
    q = deque()
    q.append((x, time))
    visited[x] = True

    while q:
        now_x, now_time = q.popleft()

        if now_x == k:
            print(now_time)

            return

        for i in (now_x * 2, now_x - 1, now_x + 1):
            if not (0 <= i <= 100000) or visited[i]:
                continue

            if i == now_x * 2:
                q.append((i, now_time))
                visited[i] = True
            else:
                q.append((i, now_time + 1))
                visited[i] = True

n, k = map(int, input().split())
visited = [False for _ in range(100001)]

bfs(n, 0)
