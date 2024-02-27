n = int(input())
a = sorted(list(map(int, input().split())))
result = 0

for i in range(len(a)):
    start = 0
    end = len(a) - 1

    while start < end: 
        sum = a[start] + a[end]

        if sum > a[i]:
            end -= 1
        elif sum < a[i]:
            start += 1
        else:
            if start == i:
                start += 1
            elif end == i:
                end -= 1
            else:
                result += 1
                break

print(result)
