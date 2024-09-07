t = int(input())
dp =  [[0 for _ in range(4)] for _ in range(100001)]
# dp[i][j] = i를 1, 2, 3의 합으로 나타내며, 마지막이 j인 방법의 수
mod = 1000000009
dp[1][1] = 1
dp[2][2] = 1
dp[3][1], dp[3][2], dp[3][3] = 1, 1, 1

for i in range(4, 100001):
    dp[i][1] = (dp[i - 1][2] + dp[i - 1][3]) % mod
    dp[i][2] = (dp[i - 2][1] + dp[i - 2][3]) % mod
    dp[i][3] = (dp[i - 3][1] + dp[i - 3][2]) % mod

for _ in range(t):
    n = int(input())
    print(sum(dp[n]) % mod)
