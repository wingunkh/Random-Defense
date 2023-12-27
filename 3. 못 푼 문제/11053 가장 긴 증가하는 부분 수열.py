n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]
# dp[i] = a[i]를 마지막 값으로 포함하는 가장 긴 증가하는 부분 수열의 길이

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
