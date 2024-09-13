def check(main_target, compare_target):
    _, g1, s1, b1 = a[main_target]
    _, g2, s2, b2 = a[compare_target]

    if g2 > g1:
        return True

    if g2 == g1 and s2 > s1:
        return True

    if g1 == g2 and s2 == s1 and b2 > b1:
        return True

    return False

n, m = map(int, input().split())
a = []

for _ in range(n):
    number, gold, silver, bronze = map(int, input().split())
    a.append((number, gold, silver, bronze))

a.sort(key = lambda x: (x[1], x[2], x[3]), reverse = True)

for i in range(n):
    if a[i][0] == m:
        target = i
        break

for i in range(n):
    if a[target][1:] == a[i][1:]:
        print(i + 1)
        break
