import sys
input = sys.stdin.readline

n = int(input())
a = [int(input()) for _ in range(n)]
dp = [0 for _ in range(n)]
# dp[i] = i번째 잔까지 선택했을 때 최대로 마실 수 있는 포도주의 양

if n < 3:
    print(sum(a))
    exit()

dp[0] = a[0]
dp[1] = a[0] + a[1]
dp[2] = max(a[0] + a[1], a[1] + a[2], a[0] + a[2])

for i in range(3, n):
    dp[i] = max(a[i] + a[i - 1] + dp[i - 3], a[i] + dp[i - 2], dp[i - 1])

print(dp[-1])
