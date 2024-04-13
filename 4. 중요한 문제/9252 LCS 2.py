import sys
sys.setrecursionlimit(10 ** 6)

a = list(input())
b = list(input())
dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) + 1)]
# dp[i][c] = 수열 a의 i번째 문자까지와 수열 b의 c번째 문자까지의 최장 공통 부분 수열
result = []

def traceback(r, c):
    if r == 0 or c == 0:
        return

    if a[r - 1] == b[c - 1]:
        result.append(a[r - 1])
        traceback(r - 1, c - 1)
    else:
        if dp[r][c - 1] > dp[r - 1][c]:
            traceback(r, c - 1)
        else:
            traceback(r - 1, c)

for r in range(1, len(a) + 1):
    for c in range(1, len(b) + 1):
        if a[r - 1] == b[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r][c - 1], dp[r - 1][c])

print(dp[len(a)][len(b)])

traceback(len(a), len(b))

print(*result[::-1], sep = '')
