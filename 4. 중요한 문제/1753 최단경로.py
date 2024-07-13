# 다익스트라 알고리즘 : 한 정점에서 다른 모든 정점까지의 최단 경로를 구할 때 사용
# 단, 가중치 중에 음수가 없어야 한다.

import sys, heapq
input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input())
a = [[] for _ in range(V + 1)] # 그래프를 인접 리스트로 구현
distance = [sys.maxsize for _ in range(V + 1)] # 출발 노드와 이외의 모든 노드 간의 최단 경로 리스트
pq = [] # 다익스트라 알고리즘은 현재까지 알고 있던 최단 경로를 토대로 최단 경로를 갱신

for _ in range(E):
    u, v, w = map(int, input().split())
    a[u].append((v, w))

distance[start] = 0 # 출발 노드에서 출발 노드까지의 최단 경로는 0
heapq.heappush(pq, (0, start)) # (가중치, 목적지)

while pq:
    weight, now = heapq.heappop(pq)

    if distance[now] < weight: # 더 이상 최단 경로가 아닌 경로일 경우 무시
        continue

    for next, weight in a[now]:
        if distance[next] > distance[now] + weight: # 최단 경로 갱신
            distance[next] = distance[now] + weight
            heapq.heappush(pq, (distance[next], next))

for i in range(1, V + 1):
    if distance[i] == sys.maxsize:
        print("INF")
    else:
        print(distance[i])
