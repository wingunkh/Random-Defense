import sys
from collections import deque
input = sys.stdin.readline

t = int(input())

def bfs():    
    q = deque()
    q.append((n, ""))
    visited[n] = True

    while q:
        now_n, result = q.popleft()

        if now_n == m:
            return result
            
        tmp = D(now_n)
        
        if not visited[tmp]:
            q.append((tmp, result + "D"))
            visited[tmp] = True

        tmp = S(now_n)
        
        if not visited[tmp]:
            q.append((tmp, result + "S"))
            visited[tmp] = True

        tmp = L(now_n)
        
        if not visited[tmp]:
            q.append((tmp, result + "L"))
            visited[tmp] = True

        tmp = R(now_n)
        
        if not visited[tmp]:
            q.append((tmp, result + "R"))
            visited[tmp] = True

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
