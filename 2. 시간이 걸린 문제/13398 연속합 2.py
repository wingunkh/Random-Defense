import sys

n = int(input())
a = list(map(int, input().split()))
dp = [[0 for _ in range(n)] for _ in range(2)]
# dp[0][i]: i번째 원소까지 고려했을 때 제거하지 않고 얻을 수 있는 최대 연속합
# dp[1][i]: i번째 원소까지 고려했을 때 한 원소를 제거해서 얻을 수 있는 최대 연속합
dp[0][0] = a[0]
dp[1][0] = -sys.maxsize
# 수는 한 개 이상 선택해야 함

for i in range(1, n):
    dp[0][i] = max(dp[0][i - 1] + a[i], a[i])
    dp[1][i] = max(dp[1][i - 1] + a[i], dp[0][i - 1])

print(max(max(dp[0]), max(dp[1])))
