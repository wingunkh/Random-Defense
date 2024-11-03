n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
# dp[i] = i번째 요소를 마지막으로 포함하는 최장 증가 수열의 길이

for i in range(n):
    dp[i] = 1
    
    for j in range(i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
