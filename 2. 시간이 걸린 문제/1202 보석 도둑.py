import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
jewel = []

for _ in range(n):
    jewel.append(tuple(map(int, input().split())))

bag = []

for _ in range(k):
    bag.append(int(input()))

jewel.sort(reverse = True)
bag.sort()
pq = []
result = 0

for i in bag:
    while jewel and jewel[-1][0] <= i:
        weight, cost = jewel.pop()
        heapq.heappush(pq, -cost)

    if pq:
        result += -heapq.heappop(pq)

print(result)
