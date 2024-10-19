s = input()
n = len(s)
a = []

for i in range(n):
    a.append(s[i:n])

for i in sorted(a):
    print(i)
