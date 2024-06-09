import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    q = deque()
    q.append((n, ""))
    visited[n] = True

    while q:
        now_n, result = q.popleft()

        if now_n == m:
            return result
            
        d = D(now_n)
        
        if not visited[d]:
            q.append((d, result + "D"))
            visited[d] = True

        s = S(now_n)
        
        if not visited[s]:
            q.append((s, result + "S"))
            visited[s] = True

        l = L(now_n)
        
        if not visited[l]:
            q.append((l, result + "L"))
            visited[l] = True

        r = R(now_n)
        
        if not visited[r]:
            q.append((r, result + "R"))
            visited[r] = True

t = int(input())

def D(n):
    return (2 * n) % 10000

def S(n):
    if n == 0:
        return 9999
    else:
        return n-1

def L(n):
    return (n % 1000) * 10 + n // 1000

def R(n):
    return (n % 10) * 1000 + n // 10

for _ in range(t):
    n, m = map(int, input().split())
    visited = [False for _ in range(10001)]

    print(bfs())
