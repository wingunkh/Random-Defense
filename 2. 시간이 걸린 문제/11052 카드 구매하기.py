n = int(input())
a = [0] + list(map(int, input().split()))
dp = [0] + [0 for _ in range(n)]
dp[1] = a[1]
# dp[i] = i개의 카드를 구매하기 위해 민규가 지불해야 하는 금액의 최댓값

for i in range(2, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], a[j] + dp[i - j])

print(dp[n])
