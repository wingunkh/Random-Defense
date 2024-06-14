import sys, heapq
input = sys.stdin.readline
result = 0

n, m, x = map(int, input().split())
a = [[] for _ in range(n + 1)]
distance = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)]
# distance[i][j] = i번 노드와 j번 노드 간 최단 경로
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

for i in range(1, n + 1):
    distance[i][i] = 0
    heapq.heappush(pq, (0, i))

    while pq:
        _, now = heapq.heappop(pq)
        
        for next, weight in a[now]:
            if distance[i][next] > distance[i][now] + weight:
                distance[i][next] = distance[i][now] + weight
                heapq.heappush(pq, (distance[i][next], next))

for i in range(1, n + 1):
    result = max(result, distance[i][x] + distance[x][i])

print(result)
