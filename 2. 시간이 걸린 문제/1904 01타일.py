n = int(input())
mod = 15746
dp = [0 for _ in range(1000001)]
# dp[i] = 타일로 만들 수 있는 길이가 n인 2진 수열의 개수
dp[1], dp[2] = 1, 2

for i in range(3, 1000001):
    dp[i] = (dp[i-1] + dp[i-2]) % mod
    # dp[i-1] 수열 뒤에 1을 붙힌 경우의 수 + dp[i-2] 수열 뒤에 00을 붙힌 경우의 수

print(dp[n])
