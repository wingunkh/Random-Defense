from copy import deepcopy

n = int(input())
a = list(map(int, input().split()))
dp = [[a[i]] for i in range(n)]
# dp[i] = a[i]를 마지막으로 포함하는 가장 긴 증가하는 부분 수열
result = []

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            if len(dp[j]) >= len(dp[i]):
                tmp = deepcopy(dp[j])
                tmp.append(a[i])
                dp[i] = tmp

for i in range(n):
    if len(dp[i]) > len(result):
        result = dp[i]

print(len(result))
print(*result)
