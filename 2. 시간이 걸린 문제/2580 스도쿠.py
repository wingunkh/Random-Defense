import sys
input = sys.stdin.readline

def check1(r, c, n):
    for i in range(9): # 행 검사
        if a[r][i] == n:
            return False

    for i in range(9): # 열 검사
        if a[i][c] == n:
            return False

    return True

def check2(r, c, n):
    r = r // 3 * 3
    c = c // 3 * 3
    
    for i in range(r, r + 3): # 사각형 검사
        for j in range(c, c + 3):
            if a[i][j] == n:
                return False

    return True

def dfs(depth):
    if depth == len(blank):
        for i in a:
            print(*i, sep = ' ')

        sys.exit()

    r, c = blank[depth]

    for i in range(1, 10):
        if check1(r, c, i) and check2(r, c, i):
            a[r][c] = i
            dfs(depth + 1)
            a[r][c] = 0    

a = [list(map(int, input().split())) for _ in range(9)]
blank = []

for r in range(9):
    for c in range(9):
        if a[r][c] == 0:
            blank.append((r, c))

dfs(0)
