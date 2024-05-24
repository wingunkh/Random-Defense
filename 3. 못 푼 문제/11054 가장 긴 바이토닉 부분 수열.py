n = int(input())
a = list(map(int, input().split()))
dp1 = [1 for _ in range(n)]
# dp[i] = a[i]를 마지막으로 포함하는 가장 큰 증가하는 부분 수열의 길이 (->)
dp2 = [1 for _ in range(n)]
# dp[i] = a[i]를 마지막으로 포함하는 가장 큰 증가하는 부분 수열의 길이 (<-)
result = 0

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

a.reverse()

for i in range(1, n):
    for j in range(i):
        if a[j] < a[i]:
            dp2[i] = max(dp2[i], dp2[j] + 1)

for i in range(n):
    result = max(result, dp1[i] + dp2[n - i - 1] - 1) # 겹치는 원소를 처리하기 위해 -1

print(result)
