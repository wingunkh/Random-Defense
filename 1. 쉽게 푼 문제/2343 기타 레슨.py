import sys

n, m = map(int, input().split())
a = list(map(int, input().split()))
left, right = max(a), sum(a)
result = sys.maxsize

while left <= right:
    center = (left + right) // 2
    tmp = 0
    count = 0

    for i in a:
        if tmp + i > center:
            count += 1
            tmp = i
        else:
            tmp += i
    else:
        if tmp:
            count += 1

    if count > m:
        left = center + 1
    else:
        result = center
        right = center - 1

print(result)
