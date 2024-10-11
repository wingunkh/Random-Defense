import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v):
    visited[v] = True

    for i in a[v]:
        if not visited[i]:
            dfs(i)
            dp[v][0] += dp[i][1]
            dp[v][1] += min(dp[i])

n = int(input())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
dp = [[0, 1] for _ in range(n + 1)]
# dp[i][0] = i번 노드가 얼리어답터가 아닐 때 필요한 최소 얼리 어답터의 수
# dp[i][1] = i번 노드가 얼리어답터일 때 필요한 최소 얼리 어답터의 수

for _ in range(n - 1):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

dfs(1)
print(min(dp[1]))
