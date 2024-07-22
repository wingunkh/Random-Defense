import sys, heapq
input = sys.stdin.readline

def dijkstra():
    pq = []
    heapq.heappush(pq, (distance[0][0], 0, 0))

    while pq:
        weight, r, c = heapq.heappop(pq)

        if weight > distance[r][c]:
            continue

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not (0 <= nr < n and 0 <= nc < m):
                continue
            
            if distance[nr][nc] > distance[r][c] + a[r][c]:
                distance[nr][nc] = distance[r][c] + a[r][c]
                heapq.heappush(pq, (distance[nr][nc], nr, nc))

m, n = map(int, input().split())
a = [list(map(int, input().rstrip())) for _ in range(n)]
distance = [[sys.maxsize for _ in range(m)] for _ in range(n)]
# distance[r][c] = r행 c열 방에 도착할 때까지 부숴야 하는 벽의 수
distance[0][0] = 0
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dijkstra()

print(distance[n - 1][m - 1])
