import sys, heapq
# heapq를 통해 우선순위 큐를 구현
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    min_heap = [] # 최소 힙
    max_heap = [] # 최대 힙
    sync = [True for _ in range(k)]
    
    for i in range(k):
        operation, n = input().split()
        n = int(n)

        if operation == 'I':
            heapq.heappush(min_heap, (n, i))
            heapq.heappush(max_heap, (-n, i))
            # heapq는 내부적으로 최소 힙을 사용하므로 배열은 오름차순 정렬됨
        else:
            if n == -1 and min_heap:
                sync[heapq.heappop(min_heap)[1]] = False
                # 최소 힙의 루트 노드는 최솟값
            elif n == 1 and max_heap:
                sync[heapq.heappop(max_heap)[1]] = False
                # 최대 힙의 루트 노드는 최댓값

            while min_heap and sync[min_heap[0][1]] == False:
                heapq.heappop(min_heap)
                
            while max_heap and sync[max_heap[0][1]] == False:
                heapq.heappop(max_heap)

    if not min_heap:
      print("EMPTY")
    else:
      print(-max_heap[0][0], min_heap[0][0])
