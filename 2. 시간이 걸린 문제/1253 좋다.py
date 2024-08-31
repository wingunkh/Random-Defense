n = int(input())
a = list(map(int, input().split()))
a.sort()
result = 0

for i in range(len(a)):
    left, right = 0, len(a) - 1

    while left < right:
        sum = a[left] + a[right]

        if sum > a[i]:
            right -= 1
        elif sum < a[i]:
            left += 1
        else:
            if left == i:
                left += 1
            elif right == i:
                right -= 1
            else:
                result += 1
                break

print(result)
