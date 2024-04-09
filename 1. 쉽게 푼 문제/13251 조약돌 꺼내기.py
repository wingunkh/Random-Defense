m = int(input())
a = list(map(int, input().split()))
k = int(input())
result = 0

for i in range(m):
    tmp = 1
    
    for j in range(k):
        tmp *= (a[i] - j) / (sum(a) - j)

    result += tmp

print(result)
