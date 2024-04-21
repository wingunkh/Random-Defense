import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def dfs(x, team):
    visited[x] = True

    if not visited[a[x]]:
        team.append(a[x])
        
        return dfs(a[x], team)
    else:
        if a[x] in team:
            return len(team[team.index(a[x]):])
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
