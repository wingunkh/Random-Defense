import sys
from collections import deque
input = sys.stdin.readline

def bfs1(r, c):
    q = deque()
    buff = [] # 최단 경로 후보 리스트
    
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        now_r, now_c, depth = q.popleft()

        if (now_r, now_c) in start:
            number = start.index((now_r, now_c))
            buff.append((now_r, now_c, depth, number))
            continue

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] == 1:
                continue

            if not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True
    if buff:
        buff.sort(key = lambda x: (x[2], x[0], x[1]))
        now_r, now_c, depth, number = buff[0]
        start[number] = (-1, -1) # 승객 탑승 처리

        return (now_r, now_c, depth, number)
    else:
        return -1

def bfs2(r, c, target):
    q = deque()
    q.append((r, c, 0))
    visited[r][c] = True

    while q:
        now_r, now_c, depth = q.popleft()

        if (now_r, now_c) == end[target]:
            return (now_r, now_c, depth)

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue

            if a[next_r][next_c] == 1:
                continue

            if not visited[next_r][next_c]:
                q.append((next_r, next_c, depth + 1))
                visited[next_r][next_c] = True

    return -1

n, m, fuel = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
taxi_r, taxi_c = map(int, input().split())
taxi_r -= 1
taxi_c -= 1
start = [0]
end = [0]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(1, m + 1):
    start_r, start_c, end_r, end_c = map(int, input().split())
    start.append((start_r - 1, start_c - 1)) # i번 손님의 출발지
    end.append((end_r - 1, end_c - 1)) # i번 손님의 목적지

for _ in range(m):
    visited = [[False for _ in range(n)] for _ in range(n)]
    buff = bfs1(taxi_r, taxi_c)

    if buff == -1:
        print(-1)
        sys.exit()

    taxi_r, taxi_c = buff[0], buff[1]
    fuel -= buff[2]

    if fuel <= 0:
        print(-1)
        sys.exit()

    visited = [[False for _ in range(n)] for _ in range(n)]
    buff = bfs2(taxi_r, taxi_c, buff[3])

    if buff == -1:
        print(-1)
        sys.exit()
        
    taxi_r, taxi_c = buff[0], buff[1]
    fuel -= buff[2]

    if fuel < 0:
        print(-1)
        sys.exit()

    fuel += buff[2] * 2

print(fuel)
