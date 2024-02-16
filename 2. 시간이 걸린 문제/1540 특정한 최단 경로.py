import sys, heapq
input = sys.stdin.readline

def dijkstra(v):
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[v] = 0
    heapq.heappush(pq, (0, v))

    while pq:
        _, now = heapq.heappop(pq)

        for next, weight in a[now]:
            if distance[next] > distance[now] + weight:
                distance[next] = distance[now] + weight
                heapq.heappush(pq, (distance[next], next))

    return distance

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))
    a[e].append((s, w))

first, second = map(int, input().split())

distance_start = dijkstra(1)
distance_first = dijkstra(first)
distance_second = dijkstra(second)

case1 = distance_start[first] + distance_first[second] + distance_second[n]
case2 = distance_start[second] + distance_second[first] + distance_first[n]

if case1 >= sys.maxsize and case2 >= sys.maxsize:
    print(-1)
else:
    print(min(case1, case2))
