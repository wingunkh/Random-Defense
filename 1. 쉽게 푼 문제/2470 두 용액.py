import sys

n = int(input())
a = sorted(list(map(int, input().split())))
left, right = 0, n - 1
sum = sys.maxsize
result = (0, 0)

while left < right:
    if abs(a[left] + a[right]) < sum:
        result = (a[left], a[right])
        sum = abs(a[left] + a[right])

    if a[left] + a[right] < 0:
        left += 1
    elif a[left] + a[right] > 0:
        right -= 1
    else:
        break

print(*result)
