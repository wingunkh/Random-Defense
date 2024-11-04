import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    if not visited[a[v]]:
        dfs(a[v])

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    result = 0

    for i in range(1, n + 1):
        if not visited[i]:
            result += 1
            dfs(i)

    print(result)
