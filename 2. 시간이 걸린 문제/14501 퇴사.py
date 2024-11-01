n = int(input())
a = [tuple(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]
# dp[i] = i일차까지 일했을 때 얻을 수 있는 최대 수익

for i in range(n):
    time, money = a[i]

    for j in range(i + time, n + 1):
        dp[j] = max(dp[j], dp[i] + money)

print(dp[-1])
