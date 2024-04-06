import sys
from collections import deque

def bfs(x):
    global result_time, result_count
    
    q = deque()
    q.append(x)
    visited[x] = 0
    
    while q:
        now_x = q.popleft()

        if now_x == k:
            if visited[now_x] <= result_time:
                result_time = visited[now_x]
                result_count += 1

        for i in (now_x - 1, now_x + 1, now_x * 2):
            if not (0 <= i <= 100000):
                continue

            if visited[i] == -1 or visited[i] >= visited[now_x] + 1: 
                q.append(i)
                visited[i] = visited[now_x] + 1

n, k = map(int, input().split())
visited = [-1 for _ in range(100001)]
result_time = sys.maxsize
result_count = 0

bfs(n)

print(result_time)
print(result_count)
