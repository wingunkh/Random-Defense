import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if a[i] == a[i + 1]:
        dp[i][i + 1] = 1

for length in range(2, n):
    for start in range(n - length):
        end = start + length

        if a[start] == a[end] and dp[start + 1][end - 1] == 1:
            dp[start][end] = 1
            
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
