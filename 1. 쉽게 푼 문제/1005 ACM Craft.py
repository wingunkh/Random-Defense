import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = [[] for _ in range(n + 1)]
    time = [0] + list(map(int, input().split()))
    indegree = [0 for _ in range(n + 1)]
    q = deque()
    dp = [0 for _ in range(n + 1)]
    # dp[i] = i번 건물을 건설하는데 걸리는 시간

    for _ in range(m):
        s, e = map(int, input().split())
        a[s].append(e)
        indegree[e] += 1

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)
            dp[i] = time[i]

    while q:
        now = q.popleft()

        for i in a[now]:
            indegree[i] -= 1
            dp[i] = max(dp[i], dp[now] + time[i])

            if indegree[i] == 0:
                q.append(i)

    target = int(input())

    print(dp[target])
