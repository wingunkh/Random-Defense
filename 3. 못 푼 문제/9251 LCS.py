a = list(input())
b = list(input())
dp = [[0 for _ in range(len(a) + 1)] for _ in range(len(b) + 1)]
# dp[i][j] = 수열 b의 i번째 문자까지와 수열 a의 j번째 문자까지의 최장 공통 부분 수열의 길이

for r in range(1, len(b) + 1):
    for c in range(1, len(a) + 1):
        if a[c - 1] == b[r - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

print(dp[len(b)][len(a)])
