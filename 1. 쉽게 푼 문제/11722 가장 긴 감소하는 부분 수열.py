n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
# dp[i] = i번째 원소를 포함하는 가장 긴 감소하는 부분 수열의 길이
dp[0] = 1

for i in range(1, n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j] + 1)
        else:
            dp[i] = max(dp[i], 1)

print(max(dp))
