from collections import deque

n = int(input())
a = [[] for _ in range(n + 1)]
time = [0]
indegree = [0 for _ in range(n + 1)]
q = deque()
dp = [0 for _ in range(n + 1)]
# dp[i] = i번 건물을 짓는데 걸리는 시간

for i in range(1, n + 1):
    buff = list(map(int, input().split()))
    buff.pop(-1)
    time.append(buff.pop(0))

    for j in buff:
        a[j].append(i)
        indegree[i] += 1

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

for i in range(1, n + 1):
    print(dp[i])
