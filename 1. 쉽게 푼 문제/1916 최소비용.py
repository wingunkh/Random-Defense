import sys
from heapq import heappush, heappop
input = sys.stdin.readline
        
n = int(input())
m = int(input())
a = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]
pq = []

for _ in range(m):
    s, e, w = map(int, input().split())
    a[s].append((e, w))

start, end = map(int, input().split())
distance[start] = 0
heappush(pq, (0, start)) # (가중치, 목적지)

while pq:
    weight, now = heappop(pq)

    if distance[now] < weight:
        continue

    for next, weight in a[now]:
        if distance[next] > distance[now] + weight:
            distance[next] = distance[now] + weight
            heappush(pq, (distance[next], next))

print(distance[end])
