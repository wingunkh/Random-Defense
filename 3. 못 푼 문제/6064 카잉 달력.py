import sys
input = sys.stdin.readline

def func(m, n, x, y):
    k = x
    
    while k <= m * n:
        if (k % n == y % n):
            return k
        
        k += m
        
    return -1

t = int(input())

for _ in range(t):
    m, n, x, y = map(int, input().split())
    print(func(m, n, x, y))
