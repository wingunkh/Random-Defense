import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split())) # 추
m = int(input())
b = list(map(int, input().split())) # 구슬
dp = [[False for _ in range(15001)] for _ in range(31)]
# dp[i][j] = i개의 추로 무게 j를 만들 수 있는지 여부
dp[0][0] = True

for i in range(1, n + 1):
    for j in range(15001):
        if dp[i - 1][j]: # 이전 단계에서 무게 j를 만들 수 있었을 경우
            # 추를 사용하지 않는 경우
            dp[i][j] = True
            
            # 추의 무게를 더하는 경우
            if j + a[i - 1] <= 15000:
                dp[i][j + a[i - 1]] = True
                
            # 추를 무게를 빼는 경우
            if abs(j - a[i - 1]) <= 15000:
                dp[i][abs(j - a[i - 1])] = True

for i in b:
    if i > 15000:
        print('N', end = ' ')
    elif dp[n][i]:
        print('Y', end = ' ')
    else:
        print('N', end = ' ')
