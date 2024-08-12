import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        now, depth = q.popleft()

        if now == 100:
            return depth

        for i in range(1, 7):
            next = now + i

            if next > 100:
                continue

            if next in ladder_snake:
                next = ladder_snake[next]

            if not visited[next]:
                q.append((next, depth + 1))
                visited[next] = True

n, m = map(int, input().split())
visited = [False for _ in range(101)]
ladder_snake = {}

for _ in range(n + m):
    start, end = map(int, input().split())
    ladder_snake[start] = end 

print(bfs())
