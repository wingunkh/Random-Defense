t = int(input())
dp = [0 for _ in range(101)]
# dp[i] = i번째 파도반 수열
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(3, 101):
    dp[i] = dp[i-2] + dp[i-3]

for _ in range(t):
    print(dp[int(input())])
