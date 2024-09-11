import sys
from collections import deque

def bfs(group):
    q = deque()
    visited = [False for _ in range(n + 1)]
    count = 0

    q.append(group[0])
    visited[group[0]] = True
    count += 1

    while q:
        now_x = q.popleft()

        for i in a[now_x]:
            if not visited[i] and i in group:
                q.append(i)
                visited[i] = True
                count += 1

    return count == len(group)

def backtracking(x, depth):
    global result

    if 0 < depth < n:
        group1 = [i for i in range(1, n + 1) if visited[i]]
        group2 = [i for i in range(1, n + 1) if not visited[i]]

        if bfs(group1) and bfs(group2):
            people1 = sum(count[i] for i in group1)
            people2 = sum(count[i] for i in group2)
            result = min(result, abs(people1 - people2))

    for i in range(x, n + 1):
        visited[i] = True
        backtracking(i + 1, depth + 1)
        visited[i] = False

n = int(input())
a = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
count = [0] + list(map(int, input().split()))
result = sys.maxsize

for i in range(1, n + 1):
    tmp = list(map(int, input().split()))

    for j in range(1, len(tmp)):
        a[i].append(tmp[j])

backtracking(1, 0)

if result == sys.maxsize:
    print(-1)
else:
    print(result)
