import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
a = [[] for _ in range(n + 1)]
indegree = [0 for _ in range(n + 1)]
q = deque()
result = []

for _ in range(m):
    tmp = list(map(int, input().split()))[1:]

    for i in range(len(tmp) - 1):
        a[tmp[i]].append(tmp[i + 1])
        indegree[tmp[i + 1]] += 1

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    result.append(now)

    for i in a[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            q.append(i)

if len(result) == n:
    print(*result, sep = "\n")
else:
    print(0)
