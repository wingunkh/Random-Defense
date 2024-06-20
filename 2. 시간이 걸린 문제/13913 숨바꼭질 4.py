from collections import deque

def trace(x):
    result = []

    while True:
        result.append(x)

        if x == n:
            return reversed(result)
        
        x = history[x]

def bfs(x):
    q = deque()
    q.append((x, 0))
    visited[x] = True

    while q:
        now_x, depth = q.popleft()

        if now_x == m:
            print(depth)
            print(' '.join(map(str, trace(now_x))))

        for next_x in (2 * now_x, now_x + 1, now_x - 1):
            if 0 <= next_x <= 100000 and not visited[next_x]:
                q.append((next_x, depth + 1))
                visited[next_x] = True
                history[next_x] = now_x

n, m = map(int, input().split())
visited = [False for _ in range(100001)]
history = [0 for _ in range(100001)]
# history[i] = i번 노드 이전의 노드 번호

bfs(n)
