n = int(input())
a = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
# dp[i] = i번째 계단을 마지막으로 밟았을 때 점수의 최댓값

for i in range(1, n + 1):
    a[i] = int(input())

dp[1] = a[1]
dp[2] = a[1] + a[2]

for i in range(3, n + 1):
    dp[i] = max(a[i] + a[i - 1] + dp[i - 3], a[i] + dp[i - 2])

print(dp[n])
