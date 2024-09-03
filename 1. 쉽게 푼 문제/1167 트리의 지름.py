import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v, length):
    visited[v] = True
    distance[v] = length

    for i in a[v]:
        if not visited[i[0]]:
            dfs(i[0], length + i[1])

n = int(input())
a = [[] for _ in range(n + 1)]
distance = [0 for _ in range(n + 1)]

for _ in range(n):
    tmp = list(map(int, input().split()))

    for i in range(1, len(tmp) - 1, 2):
        a[tmp[0]].append((tmp[i], tmp[i + 1]))


visited = [False for _ in range(n + 1)]
dfs(1, 0)

visited = [False for _ in range(n + 1)]
dfs(distance.index(max(distance)), 0)

print(max(distance))
