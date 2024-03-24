import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def bfs(r, c, mark):
    q = deque()
    q.append((r, c))
    visited[r][c] = True
    a[r][c] = mark

    while q:
        now_r, now_c = q.popleft()

        for i in range(4):
            next_r, next_c = now_r + dr[i], now_c + dc[i]

            if not (0 <= next_r < n and 0 <= next_c < m):
                continue

            if a[next_r][next_c] and not visited[next_r][next_c]:
                q.append((next_r, next_c))
                visited[next_r][next_c] = True
                a[next_r][next_c] = mark

def build_bridge(r, c, start):
    for i in range(4):
        next_r, next_c = r + dr[i], c + dc[i]
        distance = 0

        while 0 <= next_r < n and 0 <= next_c < m:
            if a[next_r][next_c] == start:
                break
            
            if a[next_r][next_c]:
                if distance >= 2:
                    edges.append((distance, start, a[next_r][next_c]))
                    
                break

            next_r, next_c = next_r + dr[i], next_c + dc[i]
            distance += 1

def find(a):
    if a == parent[a]:
        return a
    else:
        parent[a] = find(parent[a])
        
        return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a != b:
        parent[b] = a

n, m = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]

# 1. BFS를 통한 섬 구별
visited = [[False for _ in range(m)] for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
mark = 1

for r in range(n):
    for c in range(m):
        if a[r][c] and not visited[r][c]:
            bfs(r, c, mark)
            mark += 1
    
# 2. 가능한 모든 다리 건설
edges = []

for r in range(n):
    for c in range(m):
        if a[r][c]:
            build_bridge(r, c, a[r][c])

# 3. 크루스칼 알고리즘을 통한 다리 길이의 최솟값 출력
parent = [i for i in range(mark)]
count = 0
result = 0

edges.sort(key = lambda x: x[0])

for weight, start, end in edges:
    start = find(start)
    end = find(end)

    if start == end:
        continue

    union(start, end)
    count += 1
    result += weight

if count == mark - 2:
    print(result)
else:
    print(-1)
