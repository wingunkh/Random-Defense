import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[0 for _ in range(m + 1)]]
s = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
result = -sys.maxsize

for _ in range(n):
    a.append([0] + list(map(int, input().split())))

for r in range(1, n + 1):
    for c in range(1, m + 1):
        s[r][c] = s[r - 1][c] + s[r][c - 1] - s[r - 1][c - 1] + a[r][c]

for r2 in range(1, n + 1):
    for c2 in range(1, m + 1):
        for r1 in range(1, r2 + 1):
            for c1 in range(1, c2 + 1):
                prefix_sum = s[r2][c2] - s[r1 - 1][c2] - s[r2][c1 - 1] + s[r1 - 1][c1 - 1]
                result = max(result, prefix_sum)

print(result)
