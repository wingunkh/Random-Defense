import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
# dp[i][j] = i행 j열까지 도달할 수 있는 경로의 개수
dp[0][0] = 1

def func():
    for r in range(n):
        for c in range(n):
            target = a[r][c]

            if a[r][c] == 0: # 종착지에 도착했을 경우
                return dp[-1][-1]
            
            if dp[r][c] == 0: # 도달할 수 없을 경우
                continue

            if r + target < n:
                dp[r + target][c] += dp[r][c]

            if c + target < n:
                dp[r][c + target] += dp[r][c]

print(func())
