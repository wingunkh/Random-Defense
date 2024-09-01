t = int(input())

for _ in range(t):
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0 for _ in range(n)] for _ in range(2)]
    # dp[i][j] = i행 j열 스티커를 마지막으로 떼어냈을 때의 최대 점수
    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]

    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    dp[0][1] = dp[1][0] + a[0][1]
    dp[1][1] = dp[0][0] + a[1][1]

    for c in range(2, n):
        dp[0][c] = a[0][c] + max(dp[1][c - 1], dp[1][c - 2])
        dp[1][c] = a[1][c] + max(dp[0][c - 1], dp[0][c - 2])

    print(max(dp[0][-1], dp[1][-1]))
