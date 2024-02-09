import sys

n = int(input())
dp = [0 for _ in range(50001)]
# 자연수 n을 최소 개수의 제곱수 합으로 표현했을 때 항의 개수

for i in range(1, 50001):
    result = sys.maxsize
    for j in range(1, int(i ** 0.5) + 1):
        result = min(result, dp[i - j ** 2])

    dp[i] = result + 1

print(dp[n])
