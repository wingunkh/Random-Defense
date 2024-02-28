t = int(input())

for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    # dp[i][j] = j열에서 i행 스티커를 마지막으로 선택했을 때의 최대 점수
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue
    
    dp[0][1] = dp[1][0] + a[0][1]
    dp[1][1] = dp[0][0] + a[1][1]
    
    for i in range(2, n):
        dp[0][i] = a[0][i] + max(dp[1][i - 1], dp[1][i - 2])
        dp[1][i] = a[1][i] + max(dp[0][i - 1], dp[0][i - 2])

    print(max(dp[0][-1], dp[1][-1]))
