n = int(input())
a = []

for _ in range(n):
    age, name = input().split()
    a.append((int(age), name))

a.sort(key = lambda x: x[0])

for i in a:
    print(i[0], i[1])
