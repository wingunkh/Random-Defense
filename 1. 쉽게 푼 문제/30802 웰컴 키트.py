n = int(input())
a = list(map(int, input().split()))
t, p = map(int, input().split())

for i in range(6):
    if a[i] % t == 0:
        a[i] = a[i] // t
    else:
        a[i] = a[i] // t + 1

print(sum(a))
print(n // p, n % p)
