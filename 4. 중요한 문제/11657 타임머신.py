# 벨만 포드 알고리즘 : 한 정점에서 다른 모든 정점까지의 최단 경로를 구할 때 사용
# 음수 가중치 엣지가 있어도 수행 가능
# 전체 그래프에서 음수 사이클의 존재 여부를 판단 가능

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
edges = [] # 그래프를 엣지 리스트로 구현
distance = [sys.maxsize for _ in range(n + 1)] # 출발 노드와 이외의 모든 노드 간의 최단 거리 리스트
isCycle = False # 음수 사이클 존재 여부

for _ in range(m):
    s, e, w = map(int, input().split())
    edges.append((s, e, w))

distance[1] = 0 # 출발 노드에서 출발 노드까지의 최단 거리는 0

for _ in range(n - 1):
    for s, e, w in edges:
        if distance[s] != sys.maxsize and distance[e] > distance[s] + w: # 최단 거리 갱신 (출발 노드에서 s 노드까지 도달할 수 있는 경로가 존재할 경우)
            distance[e] = distance[s] + w

for s, e, w in edges: # 음수 사이클 유무를 확인하기 위해 최단 거리 재갱신
    if distance[s] != sys.maxsize and distance[e] > distance[s] + w:
        isCycle = True # 갱신되는 노드가 있다면 음수 사이클이 존재함을 의미
        break

if not isCycle:
    for i in range(2, n + 1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)
