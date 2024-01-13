def dfs(result, depth, plus, minus, multi, divide):
    global maximum, minimum

    if depth == n-1:
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        
        return

    if plus:
        dfs(result + a[depth+1], depth+1, plus-1, minus, multi, divide)
    if minus:
        dfs(result - a[depth+1], depth+1, plus, minus-1, multi, divide)
    if multi:
        dfs(result * a[depth+1], depth+1, plus, minus, multi-1, divide)
    if divide:
        dfs(int(result / a[depth+1]), depth+1, plus, minus, multi, divide-1)
        
n = int(input())
a = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())
maximum = -1000000000
minimum = 1000000000

dfs(a[0], 0, plus, minus, multi, divide)

print(maximum)
print(minimum)
