n, m = map(int, input().split())
a = list(input())
start = 0
end = m - 1
A, C, G, T = map(int, input().split())
A_COUNT = a[start:end+1].count('A')
C_COUNT = a[start:end+1].count('C')
G_COUNT = a[start:end+1].count('G')
T_COUNT = a[start:end+1].count('T')
result = 0

while True:
    if A_COUNT >= A and C_COUNT >= C and G_COUNT >= G and T_COUNT >= T:
        result += 1

    start += 1
    end += 1

    if end == len(a):
        break

    if a[start - 1] == 'A':
        A_COUNT -= 1
    elif a[start - 1] == 'C':
        C_COUNT -= 1
    elif a[start - 1] == 'G':
        G_COUNT -= 1
    else:
        T_COUNT -= 1

    if a[end] == 'A':
        A_COUNT += 1
    elif a[end] == 'C':
        C_COUNT += 1
    elif a[end] == 'G':
        G_COUNT += 1
    else:
        T_COUNT += 1

print(result)
