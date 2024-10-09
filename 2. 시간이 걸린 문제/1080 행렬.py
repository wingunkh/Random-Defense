def reverse(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            a[i][j] = 1 - a[i][j]

def func():
    count = 0
    
    if n < 3 or m < 3:
        if a == b:
            return 0
        else:
            return -1
    
    for r in range(n - 2):
        for c in range(m - 2):
            if a[r][c] != b[r][c]:
                reverse(r, c)
                count += 1

    if a == b:
        return count
    else:
        return -1

n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
b = [list(map(int, input())) for _ in range(n)]

print(func())
