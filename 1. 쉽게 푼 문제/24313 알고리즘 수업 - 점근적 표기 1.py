def func1(n):
    return a * n + b

def func2(n):
    return c * n

a, b = map(int , input().split())
c = int(input())
d = int(input())

for i in range(d, 101):
    if func1(i) > func2(i):
        print(0)
        break
else:
    print(1)
