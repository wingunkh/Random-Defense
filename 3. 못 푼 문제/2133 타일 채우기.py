n = int(input())
dp = [0 for _ in range(31)]
dp[0] = 1
dp[2] = 3

for i in range(4, n + 1, 2):
    dp[i] = dp[i - 2] * dp[2] # 일반 패턴 처리

    for j in range(4, i + 1, 2):
        dp[i] += dp[i - j] * 2 # 고유 패턴 처리

print(dp[n])
# dp[6] = dp[4] * dp[2] + dp[2] * 2 + dp[0] * 2
