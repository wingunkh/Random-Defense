def dfs(r, depth):
    global result

    if check():
        result = min(result, depth)

        return
    
    if depth == 3:
        return

    for i in range(r, h):
        for j in range(n - 1):
            if a[i][j] == 0:
                if j - 1 >= 0 and a[i][j - 1] == 1:
                    continue

                if j + 1 <= n and a[i][j + 1] == 1:
                    continue
                
                a[i][j] = 1
                dfs(i, depth + 1)
                a[i][j] = 0

def check():
    for end in range(n):
        c = end

        for r in range(h):
            if a[r][c]:
                c += 1
            elif c - 1 >= 0 and a[r][c - 1]:
                c -= 1

        if c != end:
            return False
    else:
        return True
                
n, m, h  = map(int, input().split())
a = [[0 for _ in range(n)] for _ in range(h)]
result = 4

for _ in range(m):
    x, y = map(int, input().split())
    a[x - 1][y - 1] = 1

dfs(0, 0)

if result == 4:
    print(-1)
else:
    print(result)
