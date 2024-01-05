t = int(input())
dp = [0 for _ in range(11)]
# dp[i] = 정수 i를 1, 2, 3의 합으로 나타내는 모든 경우의 수
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(1, 11):
    for j in range(1, 4):
        if i - j >= 0:
            dp[i] += dp[i-j]

for _ in range(t):
    n = int(input())

    print(dp[n])
