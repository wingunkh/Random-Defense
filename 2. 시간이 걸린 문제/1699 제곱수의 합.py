n = int(input())
dp = [i for i in range(n + 1)]
# dp[i] = i를  제곱수들의 합으로 표현할 때 필요한 항의 수의 최솟값
dp[1] = 1
    
for i in range(2, n + 1):
    for j in range(1, int(i ** 0.5) + 1):
        dp[i] = min(dp[i], 1 + dp[i - j ** 2])

print(dp[n])
