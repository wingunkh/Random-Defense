import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    result = 1
    
    for _ in range(n):
        x, y = map(int, input().split())
        a.append((x, y))

    a.sort(key = lambda x: x[0])
    tmp = a[0]
    
    for i in range(1, n):
        if a[i][1] < tmp[1]:
            tmp = a[i]
            result += 1

    print(result)
