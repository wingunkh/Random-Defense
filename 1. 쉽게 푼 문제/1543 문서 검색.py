s = input()
target = input()
left, right = 0, len(target) - 1
result = 0

while right <= len(s) - 1:
    window = s[left:right + 1]

    if window == target:
        result += 1
        left += len(target)
        right += len(target)
    else:
        left += 1
        right += 1
    
print(result)
