import sys
input = sys.stdin.readline

n = int(input())
a = [0 for _ in range(10001)]

for _ in range(n):
    number = int(input())
    a[number] += 1

for i in range(10001):
    if a[i] > 0:
        for j in range(a[i]):
            print(i)
