import sys
from collections import deque
input = sys.stdin.readline

def bfs(center):
    q = deque()

    for next, next_weight in a[start]:
        if center <= next_weight and not visited[next]:
            q.append(next)
            visited[next] = True

    while q:
        now = q.popleft()

        if now == end:
            return True

        for next, next_weight in a[now]:
            if center <= next_weight and not visited[next]:
                q.append(next)
                visited[next] = True

    return False

n, m = map(int, input().split())
a = [[] for _ in range(10001)]
result = 0

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))
    a[e].append((s, w))

start, end = map(int, input().split())
left, right = 0, 1000000001

while left <= right:
    center = (left + right) // 2
    visited = [False for _ in range(10001)]

    if bfs(center):
        result = max(result, center)
        left = center + 1
    else:
        right = center - 1

print(result)
