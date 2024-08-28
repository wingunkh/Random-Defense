import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
pq = []

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    now = heapq.heappop(pq)

    print(now, end = ' ')

    for i in a[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            heapq.heappush(pq, i)
