def check(r, c, length):
    for i in range(r, r + length):
        for j in range(c, c + length):
            if a[i][j] != a[r][c]:
                return False

    return True

def update(r, c):
    global minus_one, zero, one
    
    if a[r][c] == -1:
        minus_one += 1
    elif a[r][c] == 0:
        zero += 1
    else:
        one += 1

def func(r, c, length):
    if check(r, c, length):
        update(r, c)

        return

    length //= 3
    
    func(r, c, length)
    func(r, c + length, length)
    func(r, c + length + length, length)
    func(r + length, c, length)
    func(r + length, c + length, length)
    func(r + length, c + length + length, length)
    func(r + length + length, c, length)
    func(r + length + length, c + length, length)
    func(r + length + length, c + length + length, length)

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
minus_one, zero, one = 0, 0, 0
    
func(0, 0, n)

print(minus_one)
print(zero)
print(one)
