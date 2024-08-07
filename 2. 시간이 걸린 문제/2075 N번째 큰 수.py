import heapq

n = int(input())
pq = []

for _ in range(n):
    a = list(map(int, input().split()))

    for i in a:
        if len(pq) < n:
            heapq.heappush(pq, i)
        else:
            heapq.heappush(pq, i)
            heapq.heappop(pq)

print(pq[0])
