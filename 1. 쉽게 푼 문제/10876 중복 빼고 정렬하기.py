n = int(input())
a = sorted(set(list(map(int, input().split()))))

print(*a, sep = ' ')
