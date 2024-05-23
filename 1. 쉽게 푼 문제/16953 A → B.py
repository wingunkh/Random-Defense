from collections import deque

def bfs(x, depth):
    q = deque()
    q.append((x, depth))

    while q:
        x, depth = q.popleft()

        if x == b:
            return depth + 1

        if x > b:
            continue

        q.append((2 * x, depth + 1))
        q.append((10 * x + 1, depth + 1))

    return -1

a, b = map(int, input().split())

print(bfs(a, 0))
