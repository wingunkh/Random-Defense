n, m = map(int, input().split())
a = [list(map(int, input())) for _ in range(n)]
result = 0

def search(length):
    global result
    l = length - 1
    
    for r in range(n - l):
        for c in range(m - l):
            one, two, three, four = a[r][c], a[r][c + l], a[r + l][c], a[r + l][c + l]
            
            if one == two == three == four:
                result = length * length

                return

for length in range(1, min(n, m) + 1):
    search(length)

print(result)
