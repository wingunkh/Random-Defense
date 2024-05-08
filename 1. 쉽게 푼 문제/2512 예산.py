n = int(input())
a = sorted(list(map(int, input().split())))
budget = int(input())

left = 1
right = a[-1]

while left <= right:
    center = (left + right) // 2
    tmp = 0

    for i in a:
        if i <= center:
            tmp += i
        else:
            tmp += center

    if tmp <= budget:
        left = center + 1
    else:
        right = center - 1

print(right)
