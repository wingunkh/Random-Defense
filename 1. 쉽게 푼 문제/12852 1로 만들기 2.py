import sys
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize for _ in range(1000001)]
# dp[i] = i를 1로 만들기 위해 연산을 사용하는 횟수의 최솟값
dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, 1000001):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[n])

while n > 0:
    print(n, end = ' ')

    if dp[n - 1] + 1 == dp[n]:
        n -= 1
    elif n % 2 == 0 and dp[n // 2] + 1 == dp[n]:
        n //= 2
    else:
        n //= 3
