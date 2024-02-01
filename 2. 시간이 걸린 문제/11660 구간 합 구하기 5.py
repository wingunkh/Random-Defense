import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0 for _ in range(n+1)]]
s = [[0 for _ in range(n+1)] for _ in range(n+1)]

for _ in range(1, n+1):
    a.append([0] + list(map(int, input().split())))
    
for r in range(1, n+1):
    for c in range(1, n+1):
        s[r][c] = s[r-1][c] + s[r][c-1] - s[r-1][c-1] + a[r][c]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    print(s[x2][y2] - s[x1-1][y2] - s[x2][y1-1] + s[x1-1][y1-1])
