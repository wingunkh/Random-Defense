import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]
result_depth = 0
result_route = ""
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

start, end = map(int, input().split())
distance[start] = 0
heapq.heappush(pq, (0, start, 1, str(start)))

while pq:
    weight, now, depth, route = heapq.heappop(pq)

    if weight > distance[now]:
        continue

    if now == end:
        result_depth = depth
        result_route = route

    for next, weight in a[now]:
        if distance[now] + weight < distance[next]:
            distance[next] = distance[now] + weight
            heapq.heappush(pq, (distance[next], next, depth + 1, route + " " + str(next)))

print(distance[end])
print(result_depth)
print(result_route)
