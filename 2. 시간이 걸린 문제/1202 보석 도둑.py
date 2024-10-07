import sys, heapq
input = sys.stdin.readline

n, k = map(int, input().split())
diamond = [tuple(map(int, input().split())) for _ in range(n)]
bag = [int(input()) for _ in range(k)]
pq = []
result = 0

diamond.sort(reverse = True)
bag.sort()

for i in bag:
    while diamond and diamond[-1][0] <= i: # 가방에 넣을 수 있는 모든 다이아몬드 고려
        _, cost = diamond.pop()
        heapq.heappush(pq, -cost)

    if pq:
        result += -heapq.heappop(pq)

print(result)
