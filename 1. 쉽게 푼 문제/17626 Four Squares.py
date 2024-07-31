import sys

n = int(input())
dp = [sys.maxsize for _ in range(50001)]
# 자연수 n을 최소 개수의 제곱수 합으로 표현했을 때 항의 개수
dp[1] = 1

for i in range(2, 50001):
    int_sqrt = int(i ** 0.5)

    if i ** 0.5 == int_sqrt: # i가 어떤 수의 제곱수라면
        dp[i] = 1
    else:
        for j in range(1, int_sqrt + 1):
            dp[i] = min(dp[i], dp[j ** 2] + dp[i - j ** 2])

print(dp[n])
