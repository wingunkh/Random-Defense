a = list(map(int, input()))
n = len(a)
dp = [0 for _ in range(n + 1)]
# dp[i] = i번째 자리까지 고려했을 때 나올 수 있는 해석의 가짓수
dp[0] = 1
dp[1] = 1

if a[0] == 0:
    print(0)
else:
    for i in range(2, n + 1):
        if a[i - 1] > 0:
            dp[i] += dp[i - 1] # 현재 숫자를 한 자리 수로 해석 가능한 경우의 수 추가

        if 10 <= a[i - 2] * 10 + a[i - 1] <= 26:
            dp[i] += dp[i - 2] # 현재 숫자를 두 자리 수로 해석 가능한 경우의 수 추가

    print(dp[-1] % 1000000)
