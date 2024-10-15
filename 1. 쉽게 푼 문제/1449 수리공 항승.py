n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
start = a[0]
result = 1

for i in a[1:]:
    if start <= i <= start + m - 1:
        continue
    else:
        start = i
        result += 1
        
print(result)
