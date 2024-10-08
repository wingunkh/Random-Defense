from collections import deque

def bfs():
    q = deque()
    count = 0
    
    q.append(n)
    visited[n] = 0

    while q:
        now = q.popleft()

        if now == m:
            count += 1
            continue

        for next in (now - 1, now + 1, 2 * now):
            if not (0 <= next <= 100000):
                continue

            if visited[next] == -1 or visited[next] == visited[now] + 1:
                q.append(next)
                visited[next] = visited[now] + 1

    return count

n, m = map(int, input().split())
visited = [-1 for _ in range(100001)]
result_count = bfs()
result_time = visited[m]

print(result_time)
print(result_count)
