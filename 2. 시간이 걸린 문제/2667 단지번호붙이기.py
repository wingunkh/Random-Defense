from collections import deque

def bfs(r, c):
    q = deque()
    count = 0

    a[r][c] = 0
    q.append((r, c))
    count += 1
    
    while q:
        now_r, now_c = q.popleft()
        
        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if 0 <= next_r < n and 0 <= next_c < n and a[next_r][next_c] == 1:
                a[next_r][next_c] = 0
                q.append((next_r, next_c))
                count += 1

    return count

n = int(input())
a = [list(map(int, input())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = []

for r in range(n):
    for c in range(n):
        if a[r][c] == 1:
            result.append(bfs(r, c))

result.sort()

print(len(result))
print(*result, sep = "\n")
