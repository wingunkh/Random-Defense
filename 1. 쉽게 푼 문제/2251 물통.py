def dfs(x, y, z):
    visited[x][y] = True

    if x == 0:
        result.append(z)

    if x:
        water = min(x, b - y)
        
        if not visited[x - water][y + water]:
            dfs(x - water, y + water, z)

        water = min(x, c - z)
        
        if not visited[x - water][y]:
            dfs(x - water, y, z + water)

    if y:
        water = min(y, a - x)
        
        if not visited[x + water][y - water]:
            dfs(x + water, y - water, z)

        water = min(y, c - z)
        
        if not visited[x][y - water]:
            dfs(x, y - water, z + water)

    if z:
        water = min(z, a - x)
        
        if not visited[x + water][y]:
            dfs(x + water, y, z - water)

        water = min(z, b - y)
        
        if not visited[x][y + water]:
            dfs(x, y + water, z - water)

a, b, c = map(int, input().split())
visited = [[False for _ in range(b + 1)] for _ in range(a + 1)]
# visited[x][y] = a물통에 x, b물통에 y만큼의 물이 차 있는 상황
result = []

dfs(0, 0, c)

result.sort()

print(*result)
