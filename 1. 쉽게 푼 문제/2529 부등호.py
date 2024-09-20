def compare(x, depth):
    now = x
    prev = stack[-1]
    symbol = s[depth - 1]

    if symbol == '>':
        if now < prev:
            return True
        else:
            return False
    else:
        if now > prev:
            return True
        else:
            return False

def backtracking(depth):
    if depth == n + 1:
        result.append(''.join(map(str, stack)))
        
        return

    for i in range(0, 10):
        if visited[i]:
            continue
        
        if stack:
            if not compare(i, depth):
                continue

        stack.append(i)
        visited[i] = True
        backtracking(depth + 1)
        stack.pop()
        visited[i] = False

n = int(input())
s = input().split()
visited = [False for _ in range(10)]
stack = []
result = []

backtracking(0)

print(result[-1])
print(result[0])
