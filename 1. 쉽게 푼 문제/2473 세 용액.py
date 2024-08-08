import sys

n = int(input())
a = sorted(list(map(int, input().split())))
result_left, result_right, result_third = 0, 0, 0
result_sum = sys.maxsize

for third in range(1, n - 1):
    left, right = 0, n - 1

    while left < right:
        sum = a[left] + a[right] + a[third]

        if abs(sum) < abs(result_sum):
            result_left, result_right, result_third = left, right, third
            result_sum = sum

        if sum > 0:
            right -= 1

            if right == third:
                right -= 1
        elif sum < 0:
            left += 1

            if left == third:
                left += 1
        else:
            break

print(*sorted([a[result_left], a[result_right], a[result_third]]))
