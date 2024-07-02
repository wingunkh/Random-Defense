import sys

n = int(input())
a = list(map(int, input().split()))
left, right = 0, n - 1
result_sum = sys.maxsize
result_left, result_right = 0, 0

while left < right:
    sum = a[left] + a[right]

    if abs(sum) < abs(result_sum):
        result_sum = sum
        result_left = left
        result_right = right

    if sum > 0:
        right -= 1
    elif sum < 0:
        left += 1
    else:
        break

print(a[result_left], a[result_right])
