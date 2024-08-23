import sys, heapq
input = sys.stdin.readline

def dijkstra(v):
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[v] = 0
    heapq.heappush(pq, (0, v))

    while pq:
        now_weight, now = heapq.heappop(pq)

        if distance[now] < now_weight:
            continue

        for next, next_weight in a[now]:
            if distance[now] + next_weight < distance[next]:
                distance[next] = distance[now] + next_weight
                heapq.heappush(pq, (distance[next], next))

    return distance

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))
    a[e].append((s, w))

one, two = map(int, input().split())
pq = []

distance_start = dijkstra(1)
distance_one = dijkstra(one)
distance_two = dijkstra(two)

case1 = distance_start[one] + distance_one[two] + distance_two[n]
case2 = distance_start[two] + distance_two[one] + distance_one[n]

if case1 >= sys.maxsize and case2 >= sys.maxsize:
    print(-1)
else:
    print(min(case1, case2))
