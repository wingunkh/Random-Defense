n = int(input())
left, right = 1, 1
sum = 1
result = 0

while left <= n:
    if sum == n:
        result += 1
        sum -= left
        left += 1
        right += 1
        sum += right
    elif sum > n:
        sum -= left
        left += 1
    else:
        right += 1
        sum += right

print(result)
