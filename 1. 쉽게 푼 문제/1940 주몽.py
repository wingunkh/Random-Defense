n = int(input())
m = int(input())
a = sorted(list(map(int, input().split())))
start = 0
end = len(a) - 1
result = 0

while start < end:
    if a[start] + a[end] == m:
        result += 1
        start += 1
        end -= 1
    elif a[start] + a[end] < m:
        start += 1
    else:
        end -= 1

print(result)
