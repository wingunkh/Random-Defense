n, m = map(int, input().split())
a = list(map(int, input().split()))
left = max(a)
right = sum(a)

while left <= right:
    center = (left + right) // 2
    tmp = 0
    count = 0
    
    for i in a:
        if tmp + i > center:
            tmp = 0
            count += 1

        tmp += i
    else:
        if tmp:
            count += 1
            
    if count > m:
        left = center + 1
    else:
        right = center - 1
        
print(left)
