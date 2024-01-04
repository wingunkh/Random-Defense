n, k = map(int, input().split())
a = [i for i in range(1, n+1)]
index = 0
result = []

while a:
    index += k-1

    if index >= len(a):
        index = index % len(a)

    result.append(str(a.pop(index)))
                
print("<" + ", ".join(result) + ">")
