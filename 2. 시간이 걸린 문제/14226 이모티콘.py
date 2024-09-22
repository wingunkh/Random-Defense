from collections import deque

def bfs():
    q = deque()
    q.append((1, 0, 0))
    visited[1][0] = True

    while q:
        now_screen, now_clipboard, now_time = q.popleft()

        if now_screen == n:
            return now_time

        if not visited[now_screen][now_screen]:
            q.append((now_screen, now_screen, now_time + 1))
            visited[now_screen][now_screen] = True

        if now_clipboard > 0 and now_screen + now_clipboard < n + 1:
            if not visited[now_screen + now_clipboard][now_clipboard]:
                q.append((now_screen + now_clipboard, now_clipboard, now_time + 1))
                visited[now_screen + now_clipboard][now_clipboard] = True

        if now_screen > 0:
            if not visited[now_screen - 1][now_clipboard]:
                q.append((now_screen - 1, now_clipboard, now_time + 1))
                visited[now_screen - 1][now_clipboard] = True

n = int(input())
visited = [[False for _ in range(n + 1)] for _ in range(n + 1)]

print(bfs())
