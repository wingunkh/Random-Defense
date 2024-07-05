import sys, copy
from collections import deque

def backtracking(x, depth):
    global result
    
    if depth == m:
        result = min(result, bfs(copy.deepcopy(a)))
        
        return
        
    for i in range(x, len(virus)):
        r, c = virus[i]
        a[r][c] = 3
        backtracking(i + 1, depth + 1)
        a[r][c] = 2

def bfs(copied):
    q = deque()
    maximum = 0
            
    for r in range(n):
        for c in range(n):
            if copied[r][c] == 0: # 빈 칸 처리
                copied[r][c] = -1
            elif copied[r][c] == 1: # 벽 처리
                copied[r][c] = '-'
            elif copied[r][c] == 2: # 비활성 바이러스 처리
                copied[r][c] = '*'
            elif copied[r][c] == 3: # 활성 바이러스 처리
                copied[r][c] = 0
                q.append((r, c))

    while q:
        now_r, now_c, = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if copied[next_r][next_c] == -1: # 바이러스 증식 처리
                q.append((next_r, next_c))
                copied[next_r][next_c] = copied[now_r][now_c] + 1
                maximum = max(maximum, copied[next_r][next_c])
            elif copied[next_r][next_c] == '*': # 비활성 바이러스 통과 처리
                q.append((next_r, next_c))
                copied[next_r][next_c] = copied[now_r][now_c] + 1

    for r in range(n):
        for c in range(n):
            if copied[r][c] == -1: # 바이러스가 퍼지지 않은 빈 칸이 있을 경우
                return sys.maxsize

    return maximum

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
virus = [] # 비활성 바이러스 배열
result = sys.maxsize

for r in range(n):
    for c in range(n):
        if a[r][c] == 2:
            virus.append((r, c))
            
backtracking(0, 0)

if result == sys.maxsize:
    print(-1)
else:
    print(result)
