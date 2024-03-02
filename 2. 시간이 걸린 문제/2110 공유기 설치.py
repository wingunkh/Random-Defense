import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = sorted([int(input()) for _ in range(n)])
left = 1
right = a[-1] - a[0]
result = 0

while left <= right:
    distance = (left + right) // 2
    count = 1
    now = 0

    for i in range(1, len(a)):
        if a[i] - a[now] >= distance:
            count += 1
            now = i

    if count >= m:
        result = distance
        left = distance + 1
    else:
        right = distance - 1

print(result)
