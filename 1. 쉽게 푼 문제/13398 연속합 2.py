import sys

n = int(input())
a = list(map(int, input().split()))
dp = [[-sys.maxsize, -sys.maxsize] for _ in range(n)]
# dp[i][0] = i번째 원소까지 고려했을 때 제거하지 않고 얻을 수 있는 최대 연속합
# dp[i][1] = i번째 원소까지 고려했을 때 한 원소를 제거해서 얻을 수 있는 최대 연속합
dp[0][0] = a[0]
dp[0][1] = -sys.maxsize
result = -sys.maxsize

for i in range(1, n):
    dp[i][0] = max(dp[i - 1][0] + a[i], a[i])
    dp[i][1] = max(dp[i - 1][1] + a[i], dp[i - 1][0])

for x, y in dp:
    result = max(result, max(x, y))

print(result)
