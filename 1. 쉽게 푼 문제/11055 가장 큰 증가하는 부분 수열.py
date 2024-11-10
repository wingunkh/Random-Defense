import copy

n = int(input())
a = list(map(int, input().split()))
dp = copy.deepcopy(a)
# dp[i] = i번째 요소를 마지막으로 포함하는 가장 큰 증가하는 부분 수열의 합

for target in range(1, n):
    for i in range(target):
        if a[i] < a[target]:
            dp[target] = max(dp[target], dp[i] + a[target])

print(max(dp))
