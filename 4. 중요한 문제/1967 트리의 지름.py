import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v, distance):
    visited[v] = distance

    for next, weight in a[v]:
        if visited[next] == -1:
            dfs(next, distance + weight)

n = int(input())
a = [[] for _ in range(n + 1)]
farthest = 0

for _ in range(n - 1):
    s, e, w = map(int, input().split())
    a[s].append((e, w))
    a[e].append((s, w))

visited = [-1 for _ in range(n + 1)]
dfs(1, 0)
# 임의의 노드 (루트 노드)에서 가장 먼 노드 farthest를 탐색

farthest = visited.index(max(visited))

visited = [-1 for _ in range(n + 1)]
dfs(farthest, 0)
# 노드 farthest에서 가장 먼 노드를 탐색

print(max(visited))
# 두 노드 사이의 거리가 트리의 지름
