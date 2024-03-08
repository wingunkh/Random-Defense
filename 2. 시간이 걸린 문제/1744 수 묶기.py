import sys, heapq
input = sys.stdin.readline

n = int(input())
plus_pq = []
minus_pq = []
result = 0

for _ in range(n):
    buff = int(input())

    if buff > 0:
        heapq.heappush(plus_pq, -buff)
    else:
        heapq.heappush(minus_pq, buff)

while len(plus_pq) > 1:
    a = -heapq.heappop(plus_pq)
    b = -heapq.heappop(plus_pq)
    tmp = a + b

    if a * b > tmp:
        result += a * b
    else:
        result += a
        heapq.heappush(plus_pq, -b)

if plus_pq:
    result += -heapq.heappop(plus_pq)

while len(minus_pq) > 1:
    a = heapq.heappop(minus_pq)
    b = heapq.heappop(minus_pq)
    tmp = a + b
    result += a * b

if minus_pq:
    result += heapq.heappop(minus_pq)
    
print(result)
