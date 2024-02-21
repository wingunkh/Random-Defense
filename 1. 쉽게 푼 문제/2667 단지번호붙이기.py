import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c):
    q = deque()
    q.append((r, c))
    a[r][c] = 0
    result = 1

    while q:
        now_r, now_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] == 1:
                q.append((next_r, next_c))
                a[next_r][next_c] = 0
                result += 1

    return result

n = int(input())
a = [list(map(int, input().rstrip())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []

for r in range(n):
    for c in range(n):
        if a[r][c] == 1:
            result.append(bfs(r, c))

result.sort()

print(len(result))
print(*sorted(result), sep = "\n")
