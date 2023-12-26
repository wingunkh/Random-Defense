t = int(input())
dp = [[i for i in range(15)] for _ in range(15)]

for floor in range(1, 15):
    for room in range(1, 15):
        dp[floor][room] = dp[floor][room-1] + dp[floor-1][room]
        
for _ in range(t):
    k = int(input())
    n = int(input())

    print(dp[k][n])
