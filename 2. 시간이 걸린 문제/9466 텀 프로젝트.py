import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(v, team):
    visited[v] = True

    if not visited[a[v]]:
        team.append(a[v])

        return dfs(a[v], team)
    else:
        if a[v] in team:
            return len(team[team.index(a[v]):])
        else:
            return 0 

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int, input().split()))
    visited = [False for _ in range(n + 1)]
    result = n

    for i in range(1, n + 1):
        if not visited[i]:
            team = [i]
            result -= dfs(i, team)

    print(result)
