import sys, heapq
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
a = [[] for _ in range(n + 1)]
distance = [sys.maxsize for _ in range(n + 1)]
pq = []
flag = False

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)

distance[x] = 0
heapq.heappush(pq, (0, x))

while pq:
    now_weight, now = heapq.heappop(pq)

    if now_weight > distance[now]:
        continue

    for next in a[now]:
        if distance[now] + 1 < distance[next]:
            distance[next] = distance[now] + 1
            heapq.heappush(pq, (distance[next], next))
        
for i in range(n + 1):
    if distance[i] == k:
        flag = True
        print(i)

if not flag:
    print(-1)
