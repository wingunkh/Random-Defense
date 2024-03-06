n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
dp = [0 for _ in range(k + 1)]
# k원의 가치를 만들 수 있는 경우의 수
dp[0] = 1

for i in a:
    for j in range(i, k + 1):
        dp[j] += dp[j - i]

print(dp[k])
