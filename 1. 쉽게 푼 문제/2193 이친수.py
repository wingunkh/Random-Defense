n = int(input())
dp = [0 for i in range(91)]
# dp[i] = i자리 이친수의 개수
dp[1] = 1
dp[2] = 1

for i in range(3, 91):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[n])
