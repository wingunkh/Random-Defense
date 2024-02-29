n, k = map(int, input().split())
a = [i for i in range(1, n + 1)]
index = 0
result = []

while a:
    index = (index + (k - 1)) % len(a)
    result.append(a.pop(index))

print("<" + ', '.join(map(str, result)) + ">")
