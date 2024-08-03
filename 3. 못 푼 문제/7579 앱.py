n, m = map(int, input().split())
memory = list(map(int, input().split()))
c = list(map(int, input().split()))
a = []
dp = [[0 for _ in range(sum(c) + 1)] for _ in range(n + 1)]
# dp[i][j] = 최대 무게가 j인 가방에서 i번째 물건까지 판단했을 때의 최대 가치
# dp[i][j] = 총 코스트가 j이며 i번째 앱까지 판단했을 때의 최대 바이트 

for i in range(n):
    a.append((memory[i], c[i]))

for i in range(1, n + 1):
    for j in range(sum(c) + 1):
        cost = a[i - 1][1] # 무게 -> 코스트
        byte = a[i - 1][0] # 가치 -> 바이트

        if cost > j: # 코스트 제한에 걸릴 때
            dp[i][j] = dp[i - 1][j]
        else: # 코스트 제한에 걸리지 않을 때
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + byte)
            
for i in range(sum(c) + 1):
    if dp[n][i] >= m:
        print(i)
        break
