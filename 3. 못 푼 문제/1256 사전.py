n, m, k = map(int, input().split())
dp = [[0 for i in range(m + 1)] for _ in range(n + 1)]
# dp[i][j] = a가 i개이고 z가 j개인 문자열 조합의 총 개수
result = ""

for i in range(n + 1):
    for j in range(m + 1):
        if i == 0 or j == 0:
            dp[i][j] = 1

for i in range(1, n + 1):
    for j in range(1, m + 1):
        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

if dp[n][m] < k:
    print(-1)
else:
    while True:
        if n == 0 or m == 0:
            result += 'a' * n
            result += 'z' * m
            break

        if k <= dp[n - 1][m]: # k번째 문자열의 현재 자리가 a인 경우
            result += 'a'
            n -= 1
        else: # k번째 문자열의 현재 자리가 z인 경우
            k -= dp[n - 1][m]
            result += 'z'
            m -= 1
            
    print(result)
