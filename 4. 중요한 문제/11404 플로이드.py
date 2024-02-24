# 플로이드 알고리즘 : 모든 정점에서 다른 모든 정점까지의 최단 경로를 구할 때 사용
# 음수 가중치 엣지가 있어도 수행 가능
# 시간 복잡도가 O(V^3)으로 느리기 때문에 노드의 개수가 적을 때 사용

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
a = [[sys.maxsize for _ in range(n + 1)] for _ in range(n + 1)] # 그래프를 인접 행렬로 구현

for i in range(1, n + 1):
    a[i][i] = 0
    
for i in range(m):
    s, e, w = map(int, input().split())
    if a[s][e] > w:
        a[s][e] = w

for k in range(1, n + 1): # 경유지
    for s in range(1, n + 1): # 출발지
        for e in range(1, n + 1): # 도착지
            a[s][e] = min(a[s][e], a[s][k] + a[k][e])

for s in range(1, n + 1):
    for e in range(1, n + 1):
        if a[s][e] == sys.maxsize:
            print(0, end = ' ')
        else:
            print(a[s][e], end = ' ')
            
    print()
