n = int(input())
a = [input() for _ in range(n)]
a = list(set(a))
a.sort()
a.sort(key = lambda x: len(x))

print(*a, sep = '\n')
