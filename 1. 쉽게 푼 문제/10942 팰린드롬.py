import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[s][e] = s번째 수부터 e번째까지 수가 팰린드롬일 때 1, 아닐 때 0

for i in range(n):
    dp[i][i] = 1

for i in range(n - 1):
    if a[i] == a[i + 1]:
        dp[i][i + 1] = 1

for length in range(2, n):
    for s in range(n - length):
        e = s + length

        if a[s] == a[e] and dp[s + 1][e - 1]:
            dp[s][e] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s - 1][e - 1])
