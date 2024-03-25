# 위상 정렬 : 사이클이 없는 방향 그래프에서 노드 순서를 찾는 알고리즘
# 항상 유일한 값으로 정렬되지 않음

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)] # 그래프를 인접 리스트로 구현
indegree = [0 for _ in range(n + 1)] # 진입 차수 리스트
q = deque() # 위상 정렬 리스트

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    indegree[e] += 1 # 그래프 구현과 동시에 진입 차수 증가

for i in range(1, n + 1):
    if indegree[i] == 0: # 진입 차수가 0인 노드의 경우
        q.append(i) # 큐에 삽입

while q:
    now = q.popleft() # 진입 차수가 0인 노드를 큐에서 제거
    
    print(now, end = ' ') 

    for i in a[now]: # 큐에서 제거된 노드가 가리키는 노드들의 경우
        indegree[i] -= 1 # 진입 차수 1 감소
         
        if indegree[i] == 0:
            q.append(i)
