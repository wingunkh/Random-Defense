n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
# dp[i][j] = 길이가 i이며 j로 끝나는 오르막 수의 개수

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for j in range(10):
        for k in range(j + 1):
            dp[i][j] += dp[i - 1][k]

print(sum(dp[n]) % 10007)
