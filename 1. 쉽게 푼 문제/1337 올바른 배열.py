import sys
input = sys.stdin.readline

def check(start, length):
    target = [i for i in range(a[start], a[start] + 5)]
    window = a[start:start + length]
    count = 5

    for i in window:
        if i in target:
            count -= 1

    return count

n = int(input())
a = sorted([int(input()) for _ in range(n)])
result = sys.maxsize

if n < 5:
    result = min(result, check(0, n))
else:
    for i in range(n - 1):
        result = min(result, check(i, 5))

print(result)
