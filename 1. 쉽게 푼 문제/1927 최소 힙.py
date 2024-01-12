import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    buff = int(input())

    if buff == 0:
        if a:
            print(heapq.heappop(a))
        else:
            print(0)
    else:
        heapq.heappush(a, buff)
