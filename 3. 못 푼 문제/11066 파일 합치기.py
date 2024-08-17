import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = [0] + list(map(int ,input().split()))
    s = [0 for _ in range(n + 1)]
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    # dp[i][j] = i번째 파일부터 j번째 파일까지 하나의 파일로 합칠 때 필요한 최소 비용

    for i in range(1, n + 1):
        s[i] = s[i - 1] + a[i]

    for length in range(1, n + 1): # 부분 파일의 길이
        for start in range(1, n + 1 - length):
            end = start + length
            dp[start][end] = sys.maxsize
                    
            for i in range(start, end):
                dp[start][end] = min(dp[start][end], dp[start][i] + dp[i + 1][end] + s[end] - s[start - 1])
                # ex) 2번째 파일 ~ 4번째 파일 최소 비용
                # min(2번째 파일 ~ 3번째 파일 + 4번째 파일, 3번째 파일 ~ 4번째 파일 + 2번째 파일)
                # = min(2번째 파일 ~ 3번째 파일, 3번째 파일 ~ 4번째 파일) + 2번째 파일 ~ 4번째 파일
            
    print(dp[1][n])
