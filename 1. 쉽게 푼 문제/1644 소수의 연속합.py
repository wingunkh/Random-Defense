n = int(input())
a = [i for i in range(n + 1)]
a[1] = 0
prime = []
result = 0

for i in range(2, int(n ** 0.5) + 1):
    if a[i] == 0:
        continue
    
    for j in range(i + i, len(a), i):
        a[j] = 0

for i in a:
    if i != 0:
        prime.append(i)

start, end = 0, 0

while end <= len(prime) - 1:
    target = sum(prime[start : end + 1])

    if target == n:
        result += 1
        start += 1
        end += 1
    elif target > n:
        start += 1
    else:
        end += 1

print(result)
