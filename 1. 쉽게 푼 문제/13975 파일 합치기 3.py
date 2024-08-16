import sys, heapq
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int ,input().split()))
    pq = []
    result = 0

    for i in a:
        heapq.heappush(pq, i)

    while len(pq) > 1:
        x = heapq.heappop(pq)
        y = heapq.heappop(pq)
        sum = x + y

        result += sum
        heapq.heappush(pq, sum)
        
    print(result)
