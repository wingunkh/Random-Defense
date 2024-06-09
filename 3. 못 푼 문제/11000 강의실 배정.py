import sys, heapq
input = sys.stdin.readline

n = int(input())
a = []
q = []

for _ in range(n):
    s, e = map(int, input().split())
    a.append((s, e))

a.sort(key = lambda x: (x[0], x[1]))
heapq.heappush(q, a[0][1])

for i in range(1, n):
    if a[i][0] < q[0]: # 다음 수업의 시작 시간이 현재 수업의 종료 시간보다 빠를 경우
        heapq.heappush(q, a[i][1])
    else: # 다음 수업의 시작 시간이 현재 수업의 종료 시간보다 느리거나 같을 경우
        heapq.heappop(q)
        heapq.heappush(q, a[i][1])

print(len(q))
