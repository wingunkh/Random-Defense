n = int(input())
buff = list(map(int, input().split()))
a = [i for i in range(1001)]
result = 0

a[1] = 0

for i in range(2, int(len(a) ** 0.5)+1):
    if a[i] == 0:
        continue
    
    for j in range(i+i, len(a), i):
        a[j] = 0

for i in buff:
    if a[i] != 0:
        result += 1

print(result)
