n = int(input())
dp = [[0 for _ in range(10)] for _ in range(n + 1)]
# dp[i][j] = 길이가 i이며 j로 끝나는 오르막 수의 개수

for i in range(10):
    dp[1][i] = 1

for i in range(2, n + 1):
    for a in range(10):
        for b in range(a, 10):
            dp[i][b] += dp[i - 1][a]
            # ex) dp[1][2] = 2
            # 즉, 길이가 1이며 2로 끝나는 오르막 수의 개수가 2일 경우
            # dp[2][2], dp[2][3], ... , dp[2][9]의 개수를 2씩 추가

print(sum(dp[n]) % 10007)
