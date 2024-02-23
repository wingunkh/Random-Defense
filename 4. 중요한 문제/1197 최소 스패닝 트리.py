# 크루스칼 알고리즘 : 그래프 내의 모든 정점을 가장 적은 비용으로 연결하기 위해 사용
# 즉, 최소 신장 트리를 구하기 위한 알고리즘
# 유니온 파인드를 통해 사이클 존재 여부를 판단

import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a != b:
        parent[b] = a

v, e = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(e)]
parent = [i for i in range(v + 1)]
result = 0

edges.sort(key = lambda x: x[2])
# 엣지를 가중치를 기준으로 오름차순 정렬

for start, end, weight in edges:
    start = find(start)
    end = find(end)
    
    if start == end: # 루트 노드가 같다면 사이클이 존재함을 의미
        continue

    union(start, end)
    result += weight

print(result)
