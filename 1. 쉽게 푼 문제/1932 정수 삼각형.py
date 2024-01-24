import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * i for i in range(1, n+1)]
# dp[i][j] = 삼각형의 i번째 행, j번째 열에 도달했을 때의 최대 합
dp[0][0] = a[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j == 0:
            dp[i][j] = a[i][j] + dp[i-1][j]
        elif 1 <= j <= i-1:
            dp[i][j] = a[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        else:
            dp[i][j] = a[i][j] + dp[i-1][j-1]

print(max(dp[n-1]))
