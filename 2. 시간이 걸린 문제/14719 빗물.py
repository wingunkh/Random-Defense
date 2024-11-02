h, w = map(int, input().split())
a = list(map(int, input().split()))
result = 0

for i in range(1, w - 1):
    left_max = max(a[:i])
    right_max = max(a[i + 1:])
    possible = min(left_max, right_max)

    if possible > a[i]:
        result += possible - a[i]

print(result)
