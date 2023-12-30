n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]
# dp[i] = i번째 수를 마지막 값으로 포함하는 연속합의 최댓값
dp[0] = a[0]

for i in range(1, n):
    dp[i] = max(dp[i-1] + a[i], a[i])

print(max(dp))    
