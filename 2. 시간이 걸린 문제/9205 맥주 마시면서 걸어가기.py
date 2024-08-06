from collections import deque

def bfs():
    q = deque()
    q.append((home[0], home[1]))

    while q:
        now_x, now_y = q.popleft()

        if abs(dest[0] - now_x) + abs(dest[1] - now_y) <= 1000:
            return "happy"

        for i in range(n):
            if not visited[i] and abs(store[i][0] - now_x) + abs(store[i][1] - now_y) <= 1000:
                q.append((store[i][0], store[i][1]))
                visited[i] = True

    return "sad"

t = int(input())

for _ in range(t):
    n = int(input())
    home = list(map(int, input().split()))
    store = [list(map(int, input().split())) for _ in range(n)]
    visited = [False for _ in range(n)]
    dest = list(map(int, input().split()))

    print(bfs())
