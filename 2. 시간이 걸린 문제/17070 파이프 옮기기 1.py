import sys
input = sys.stdin.readline

def dfs(r, c, d):
    count = 0
    
    if (r, c, d) in cache:
        return cache[(r, c, d)]
    
    if r == n - 1 and c == n - 1:
        return 1

    if d == 0:
        direction = directions[0]
    elif d == 1:
        direction = directions[1]
    else:
        direction = directions[2]
    
    for i in range(len(direction)):
        dr, dc = direction[i]
        nr, nc = r + dr, c + dc

        if not (0 <= nr < n and 0 <= nc < n):
            continue

        if a[nr][nc] == 1:
            continue

        if dr == 1 and dc == 1:
            if a[nr - 1][nc] == 1 or a[nr][nc - 1] == 1:
                continue
        
        if dr == 0 and dc == 1:
            count += dfs(nr, nc, 0)
        elif dr == 1 and dc == 0:
            count += dfs(nr, nc, 1)
        else:
            count += dfs(nr, nc, 2)

    cache[(r, c, d)] = count

    return count

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
directions = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [(0, 1), (1, 1), (1, 0)]]
cache = {}

print(dfs(0, 1, 0))
