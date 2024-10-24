n = int(input())
dp = [i for i in range(n + 1)]
# dp[i] = i를  제곱수들의 합으로 표현할 때 필요한 항의 수의 최솟값
dp[1] = 1

for i in range(2, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])
        # ex) dp[10]
        # 1^2 + dp[9] or 2^2 + dp[6] or 3^2 + dp[1]

print(dp[n])
