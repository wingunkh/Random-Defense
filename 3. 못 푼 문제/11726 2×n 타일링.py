n = int(input())
dp = [0 for _ in range(1001)]
# dp[i] = 2×i 크기의 직사각형을 타일로 채우는 경우의 수
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])
