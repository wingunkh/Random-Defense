t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
sub_a = {}
sub_b = {}
result = 0

for i in range(n):
    tmp = 0

    for j in range(i, n):
        tmp += a[j]

        if tmp not in sub_a:
            sub_a[tmp] = 1
        else:
            sub_a[tmp] += 1

for i in range(m):
    tmp = 0

    for j in range(i, m):
        tmp += b[j]
        
        if tmp not in sub_b:
            sub_b[tmp] = 1
        else:
            sub_b[tmp] += 1

for i in sub_a:
    target = t - i

    if target in sub_b:
        result += sub_a[i] * sub_b[target]

print(result)
