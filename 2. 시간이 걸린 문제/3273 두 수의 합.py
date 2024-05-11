n = int(input())
a = sorted(list(map(int, input().split())))
target = int(input())
left = 0
right = n - 1
result = 0

while left < right:
    sum = a[left] + a[right]
    
    if sum == target:
        result += 1
        left += 1
        right -= 1
    elif sum < target:
        left += 1
    else:
        right -= 1
    
print(result)
