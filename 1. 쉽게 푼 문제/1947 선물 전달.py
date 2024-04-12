n = int(input())
dp = [0 for _ in range(1000001)]
dp[2] = 1

for i in range(3, 1000001):
    dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % 1000000000

print(dp[n])
