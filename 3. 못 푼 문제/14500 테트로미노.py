def dfs(r, c, depth, sum):
    global result

    if depth == 4:
        result = max(result, sum)
        
        return

    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]

        if not (0 <= next_r < n and 0 <= next_c < m):
            continue
        
        if not visited[next_r][next_c]:
            visited[next_r][next_c] = True
            dfs(next_r, next_c, depth + 1, sum + a[next_r][next_c])
            visited[next_r][next_c] = False

def func(r, c):
    global result

    for i in range(4):
        tmp = a[r][c]
        
        for j in range(3):
            next_r, next_c = r + dr[(i + j) % 4], c + dc[(i + j) % 4]
            
            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            tmp += a[next_r][next_c]

        result = max(result, tmp)

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r, c, 1, a[r][c])
        visited[r][c] = False

        func(r, c)

print(result)
