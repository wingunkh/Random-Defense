import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [[0 for i in range(1001)] for _ in range(1001)]
# dp[i][j] = i개 중 j를 선택하는 경우의 수

for i in range(1001):
    dp[i][0] = 1
    dp[i][1] = i
    dp[i][i] = 1

for i in range(2, 1001):
    for j in range(2, i):
        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % 10007

print(dp[n][k])
