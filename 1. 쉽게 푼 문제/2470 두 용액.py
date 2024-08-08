import sys

n = int(input())
a = sorted(list(map(int, input().split())))
left, right = 0, n - 1
result_left, result_right = 0, 0
result_sum = sys.maxsize

while left < right:
    sum = a[left] + a[right]
    
    if abs(sum) < abs(result_sum):
        result_left, result_right = left, right
        result_sum = sum

    if sum < 0:
        left += 1
    elif sum > 0:
        right -= 1
    else:
        break

print(a[result_left], a[result_right])
