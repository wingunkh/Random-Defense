n, k = map(int, input().split())
a = []
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
# dp[i][j] = i번째 물건까지 고려했을 때, 최대 무게가 j인 가방에 담을 수 있는 최대 가치

for _ in range(n):
    w, v = map(int, input().split())
    a.append((w, v))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight, value = a[i - 1][0], a[i - 1][1]

        if weight > j: # 가방에 물건을 넣을 수 없을 때
            dp[i][j] = dp[i - 1][j]
        else: # 가방에 물건을 넣을 수 있을 때
            dp[i][j] = max(dp[i - 1][j - weight] + value, dp[i - 1][j])
            # dp[i - 1][j - weight] + value = 물건을 담는 경우
            # dp[i - 1][j] = 물건을 담지 않는 경우

print(dp[n][k])
