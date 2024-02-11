import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((1, 0))
    visited[1] = True

    while q:
        x, depth = q.popleft()
        
        if x == 100:
            return depth

        for i in range(1, 7):
            next = x + i
            
            if next <= 100:
                if next in a:
                    next = a[next]

                if not visited[next]:
                    q.append((next, depth + 1))
                    visited[next] = True

n, m = map(int, input().split())
visited = [False for _ in range(101)]
a = dict()

for _ in range(n + m):
    s, e = map(int, input().split())
    a[s] = e

print(bfs())
