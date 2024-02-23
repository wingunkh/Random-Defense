def dfs(x, depth):
    if depth == n:
        if check():
            print(*result, sep = '')

        return

    for i in range(x, m):
        result.append(s[i])
        dfs(i + 1, depth + 1)
        result.pop()

def check():
    count = 0

    for i in result:
        if i in a:
            count += 1

    if count >= 1 and n - count >= 2:
        return True
    else:
        return False
    
n, m = map(int, input().split())
s = sorted(list(input().split()))
a = ['a', 'i', 'e', 'o', 'u']
result = []

dfs(0, 0)
