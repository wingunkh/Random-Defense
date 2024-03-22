import sys, heapq
input = sys.stdin.readline

n, m, k = map(int, input().split())
a = [[] for _ in range(n + 1)]
distance = [[sys.maxsize for _ in range(k)] for _ in range(n + 1)]
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

distance[1][0] = 0
heapq.heappush(pq, (0, 1))

while pq:
    now_weight, now = heapq.heappop(pq)

    for next, weight in a[now]:
        sum = now_weight + weight # 현재 노드까지의 가중치 + 현재 노드에서 다음 노드까지의 가중치

        if distance[next][k - 1] > sum:
            distance[next][k - 1] = sum
            distance[next].sort()
            heapq.heappush(pq, (sum, next))

for i in range(1, n + 1):
    if distance[i][k - 1] == sys.maxsize:
        print(-1)
    else:
        print(distance[i][k - 1])
