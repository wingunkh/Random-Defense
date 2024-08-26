import sys, heapq
input = sys.stdin.readline

def dijkstra():
    distance[0][0] = a[0][0]
    heapq.heappush(pq, (distance[0][0], 0, 0))

    while pq:
        now_weight, now_r, now_c = heapq.heappop(pq)

        if distance[now_r][now_c] < now_weight:
            continue

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < n):
                continue
            
            if distance[now_r][now_c] + a[next_r][next_c] < distance[next_r][next_c]:
                distance[next_r][next_c] = distance[now_r][now_c] + a[next_r][next_c]
                heapq.heappush(pq, (distance[next_r][next_c], next_r, next_c))

count = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
pq = []

while True:
    n = int(input())
    tmp = []
    a = [list(map(int, input().split())) for _ in range(n)]
    distance = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    
    if n == 0:
        break
    else:
        count += 1

    dijkstra()

    print(f"Problem {count}: {distance[n - 1][n - 1]}")
