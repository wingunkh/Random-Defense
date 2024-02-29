def dfs(depth):
    if depth == n:
        print(''.join(map(str, result)))

        return

    for i in range(1, 10):
        result.append(i)
        
        if is_prime(int(''.join(map(str, result)))):
            dfs(depth + 1)
            
        result.pop()

def is_prime(n):
    if n == 1:
        return False
    
    for i in range(2, int(n ** (0.5)) + 1):
        if n % i == 0:
            return False
    else:
        return True

n = int(input())
result = []

dfs(0)
