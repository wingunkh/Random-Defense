import sys
input = sys.stdin.readline

t = int(input())
a = [i for i in range(10001)]
a[1] = 0

for i in range(2, 101):
    if a[i] == 0:
        continue

    for j in range(i + i, 10001, i):
        a[j] = 0

for _ in range(t):
    n  = int(input())
    left, right = n // 2, n // 2

    while True:
        if a[left] != 0 and a[right] != 0:
            break
        
        left -= 1
        right += 1
    
    print(left, right)
