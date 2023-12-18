from collections import deque

def bfs():
    q = deque()
    q.append(n)

    while q:
        now = q.popleft()

        if now == m:
            print(visited[now])
            break

        for i in (now-1, now+1, now*2):
            if 0 <= i <= 100000 and not visited[i]:
                visited[i] = visited[now] + 1
                q.append(i)
            
n, m = map(int, input().split())
visited = [0 for _ in range(100001)]

bfs()
