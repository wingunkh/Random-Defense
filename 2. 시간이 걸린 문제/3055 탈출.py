from collections import deque

def water():
    q = deque()

    for r in range(n):
        for c in range(m):
            if a[r][c] == '*':
                q.append((r, c))
                a[r][c] = 0

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]
            
            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == '.':
                q.append((next_r, next_c))
                a[next_r][next_c] = a[now_r][now_c] + 1

def hedgehog(r, c, depth):
    q = deque()
    q.append((r, c, depth))

    while q:
        now_r, now_c, depth = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]
                        
            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] == 'X':
                continue

            if a[next_r][next_c] == 'D':
                return depth + 1

            if a[next_r][next_c] == '.' or depth + 1 < a[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                a[next_r][next_c] = 'X'

    return "KAKTUS"

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for r in range(n):
    for c in range(m):
        if a[r][c] == 'S':
            start_r, start_c = r, c
            a[r][c] = '.'

water()
print(hedgehog(start_r, start_c, 0))
