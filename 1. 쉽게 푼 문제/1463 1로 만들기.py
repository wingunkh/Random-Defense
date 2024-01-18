n = int(input())
dp = [0 for _ in range(n+1)]
# dp[i] = 정수 i를 1로 만드는 최소 연산 횟수

for i in range(2, n+1):
    dp[i] = 1 + dp[i-1]
    
    if i % 3 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 3])
    if i % 2 == 0:
        dp[i] = min(dp[i], 1 + dp[i // 2])
        
print(dp[n])
