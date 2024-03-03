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
    buff = list(map(int, input().split()))
    node = buff[0]
    buff = buff[1:-1]

    for j in range(0, len(buff), 2):
        a[node].append((buff[j], buff[j + 1]))

visited = [False for _ in range(n + 1)]
dfs(1, 0)

visited = [False for _ in range(n + 1)]
dfs(distance.index(max(distance)), 0)

print(max(distance))
