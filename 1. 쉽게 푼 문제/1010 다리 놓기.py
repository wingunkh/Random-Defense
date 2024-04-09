t = int(input())
dp = [[0 for _ in range(31)] for _ in range(31)]
# dp[i][j] = i개 중 j를 선택하는 경우의 수

for i in range(1, 31):
    dp[i][0] = 1
    dp[i][1] = i
    dp[i][i] = 1

for i in range(2, 31):
    for j in range(2, 31):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

for _ in range(t):
    n, m = map(int, input().split())

    print(dp[m][n])
