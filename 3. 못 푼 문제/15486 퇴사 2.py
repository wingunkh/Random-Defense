import sys
input = sys.stdin.readline

n = int(input())
a = []
dp = [0 for _ in range(n + 1)]
# dp[i] = i번째 날 퇴사했을 때 얻을 수 있는 최대 수익

for _ in range(n):
    time, money = map(int, input().split())
    a.append((time, money))

for i in range(1, n + 1):
    dp[i] = max(dp[i], dp[i - 1])
    # 그 전날까지 얻은 최대 수익을 그대로 유지
    time, money = a[i - 1]

    if i + time - 1 < n + 1:
        dp[i + time - 1] = max(dp[i + time - 1], dp[i - 1] + money)
        # 상담은 i번째 날에 시작함
        # 즉, i - 1번째 날까지의 최대 수익에 현재 상담에서 얻는 수익을 더해야 함

print(dp[-1])
