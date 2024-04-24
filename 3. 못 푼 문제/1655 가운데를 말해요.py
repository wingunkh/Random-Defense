import sys, heapq
input = sys.stdin.readline

n = int(input())
maxheap = [] # 중간값은 항상 maxheap의 루트 노드에 위치하도록 구현
minheap = []

for _ in range(n):
    if len(minheap) == len(maxheap):
        heapq.heappush(maxheap, -int(input()))
    else:
        heapq.heappush(minheap, int(input()))

    if minheap and minheap[0] < -maxheap[0]:
        # maxheap의 루트 노드가 minheap의 루트 노드보다 크다면
        tmp1 = heapq.heappop(maxheap)
        tmp2 = heapq.heappop(minheap)
        
        heapq.heappush(maxheap, -tmp2)
        heapq.heappush(minheap, -tmp1)
        # 두 루트 노드를 교체

    print(-maxheap[0])
