n = int(input())
a = list(map(int, input().split()))
maximum = max(a)

for i in range(len(a)):
    a[i] = a[i] / maximum * 100

print(sum(a) / len(a))
