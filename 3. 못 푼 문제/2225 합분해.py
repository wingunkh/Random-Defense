n, k = map(int, input().split())
dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
# dp[a][b] = a를 b개의 정수의 합으로 나타내는 방법의 수

for i in range(1, k + 1):
    dp[0][i] = 1
    # 0을 i개의 정수의 합으로 나타내는 방법의 수는 1
    # ex) dp[0][3] = [0, 0, 0]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # ex) dp[3][3] = dp[2][3] + dp[3][2] 인 이유
        # dp[2][3] = "2를 3개의 정수 합으로 나타내는 방법의 수"의 마지막 숫자에 1을 더한 경우
        # dp[3][2] = "3을 2개의 정수 합으로 나타내는 방법의 수"의 마지막 숫자가 0인 경우

print(dp[n][k] % 1000000000)
