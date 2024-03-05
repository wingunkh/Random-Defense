import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = [int(input()) for _ in range(n)]
dp = [sys.maxsize for _ in range(k + 1)]
# k원의 가치를 만들 수 있는 최소한의 동전 개수
dp[0] = 0

for i in a:
    for j in range(i, k + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)

if dp[k] == sys.maxsize:
    print(-1)
else:
    print(dp[k])
