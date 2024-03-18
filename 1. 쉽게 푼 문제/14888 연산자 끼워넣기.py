import sys

def dfs(result, plus, minus, multiple, divide, index):
    global minimum, maximum
    
    if index == n:
        minimum = min(minimum, result)
        maximum = max(maximum, result)
        
        return

    if plus:
        dfs(result + a[index], plus - 1, minus, multiple, divide, index + 1)

    if minus:
        dfs(result - a[index], plus, minus - 1, multiple, divide, index + 1)

    if multiple:
        dfs(result * a[index], plus, minus, multiple - 1, divide, index + 1)

    if divide:
        dfs(int(result / a[index]), plus, minus, multiple, divide - 1, index + 1)

n = int(input())
a = list(map(int, input().split()))
plus, minus, multiple, divide = map(int, input().split())
minimum = sys.maxsize
maximum = -sys.maxsize

dfs(a[0], plus, minus, multiple, divide, 1)

print(maximum)
print(minimum)
