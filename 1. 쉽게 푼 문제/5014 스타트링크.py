from collections import deque

def bfs(x):
    q = deque()
    q.append((x, 0))

    while q:
        now, count = q.popleft()

        if now == end:
            return count

        if now + up <= height and not visited[now + up]:
            q.append((now + up, count + 1))
            visited[now + up] = True

        if now - down >= 1 and not visited[now - down]:
            q.append((now - down, count + 1))
            visited[now - down] = True

    return "use the stairs"

height, start, end, up, down = map(int, input().split())
visited = [False for _ in range(1000001)]
        
print(bfs(start))
