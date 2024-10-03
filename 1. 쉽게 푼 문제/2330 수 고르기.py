import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = [int(input()) for _ in range(n)]
a.sort()
left, right = 0, 0
result = sys.maxsize

while right <= n - 1:
    gap = a[right] - a[left]

    if gap == m:
        result = m
        break
    elif gap > m:
        result = min(result, gap)
        left += 1
    else:
        right += 1

print(result)
