n, mod = map(int, input().split())
a = list(map(int, input().split()))
s = []
tmp = 0
remainder = [0 for _ in range(mod)]
result = 0

for i in a:
    tmp += i
    s.append(tmp % mod)

for i in s:
    if i == 0:
        result += 1
        
    remainder[i] += 1

for i in remainder:
    if i > 1:
        result += i * (i - 1) // 2
        # (a - b) % mod = 0 -> (a % mod - b % mod) % mod = 0
        # (a % mod - b % mod) % mod = 0 -> a % mod == b % mod

print(result)
