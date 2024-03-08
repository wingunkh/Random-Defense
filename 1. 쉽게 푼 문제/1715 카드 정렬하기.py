import sys, heapq
input = sys.stdin.readline

n = int(input())
pq = []
result = 0

for _ in range(n):
    heapq.heappush(pq, int(input()))

while len(pq) > 1:
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    tmp = a + b
    result += tmp
    heapq.heappush(pq, tmp)

print(result)
