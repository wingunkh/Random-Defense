import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []

for _ in range(n):
    buff = int(input())

    if buff:
        heapq.heappush(a, (abs(buff), buff))
    else:
        if a:
            print(heapq.heappop(a)[1])
        else:
            print(0)
