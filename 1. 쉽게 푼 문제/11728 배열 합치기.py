n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
result = []
a_pointer, b_pointer = 0, 0

while a_pointer < n and b_pointer < m:
    if a[a_pointer] <= b[b_pointer]:
        result.append(a[a_pointer])
        a_pointer += 1
    else:
        result.append(b[b_pointer])
        b_pointer += 1

if a_pointer < n:
    for i in range(a_pointer, n):
        result.append(a[i])
elif b_pointer < m:
    for i in range(b_pointer, m):
        result.append(b[i])
        
print(*result)
