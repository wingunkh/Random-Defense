a = input()
s = set()

for length in range(1, len(a) + 1):
    for start in range(len(a) - length + 1):
        s.add(a[start:start + length])

print(len(s))
