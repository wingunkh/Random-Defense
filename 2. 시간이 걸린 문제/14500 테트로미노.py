import sys
input = sys.stdin.readline

def dfs(r, c, sum, depth):
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
            dfs(next_r, next_c, sum + a[next_r][next_c], depth + 1)
            visited[next_r][next_c] = False

def func(r, c):
    global result
    
    for i in range(4):
        sum = a[r][c]
        
        for j in range(3):
            next_r, next_c = r + dr[(j + i) % 4], c + dc[(j + i) % 4]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            sum += a[next_r][next_c]

        result = max(result, sum)
    
n, m = map(int, input().split())
a = []
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
result = 0

for _ in range(n):
    a.append(list(map(int, input().split())))

for r in range(n):
    for c in range(m):
        visited[r][c] = True
        dfs(r, c, a[r][c], 1)
        visited[r][c] = False

        func(r, c)

print(result)
