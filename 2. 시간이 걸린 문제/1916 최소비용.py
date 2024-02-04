import sys, heapq
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
distance = [sys.maxsize for _ in range(n+1)]
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

start, end = map(int, input().split())
distance[start] = 0
heapq.heappush(pq, (0, start))

while pq:
    _, now = heapq.heappop(pq)

    if visited[now]:
        continue

    visited[now] = True

    for next, weight in a[now]:
        if distance[next] > distance[now] + weight:
            distance[next] = distance[now] + weight
            heapq.heappush(pq, (distance[next], next))

print(distance[end])
