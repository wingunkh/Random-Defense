n = int(input())
a = []
dp = [1 for _ in range(n)]
# dp[i] = i번째 전깃줄을 포함하는 결과의 최댓값

for _ in range(n):
    x, y = map(int, input().split())
    a.append((x, y))

a.sort(key = lambda x: x[0])

for i in range(1, n):
    for j in range(i):
        if a[j][1] < a[i][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
