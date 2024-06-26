n, k = map(int, input().split())
password = list(input())
start = 0
end = k - 1
A = password[:end + 1].count('A')
C = password[:end + 1].count('C')
G = password[:end + 1].count('G')
T = password[:end + 1].count('T')
AA, CC, GG, TT = map(int, input().split())
result = 0

while True:
    if A >= AA and C >= CC and G >= GG and T >= TT:
        result += 1
 
    start += 1
    end += 1

    if end == n:
        break

    if password[start - 1] == 'A':
        A -= 1
    elif password[start - 1] == 'C':
        C -= 1
    elif password[start - 1] == 'G':
        G -= 1
    else:
        T -= 1

    if password[end] == 'A':
        A += 1
    elif password[end] == 'C':
        C += 1
    elif password[end] == 'G':
        G += 1
    else:
        T += 1

print(result)
