n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
# dp[i] = a[i]를 마지막으로 포함하는 가장 큰 증가하는 부분 수열의 합
dp[0] = a[0]

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + a[i])
        else:
            dp[i] = max(dp[i], a[i])

print(max(dp))
