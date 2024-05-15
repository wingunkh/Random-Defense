n = int(input())
a = []
dp = [0 for _ in range(n + 1)]
# dp[i] = i 일차까지 일했을 때 얻을 수 있는 최대 수익

for _ in range(n):
    time, money = map(int, input().split())
    a.append((time, money))

for i in range(n):
    for j in range(i + a[i][0], n + 1):
        dp[j] = max(dp[j], dp[i] + a[i][1])

print(dp[-1])
