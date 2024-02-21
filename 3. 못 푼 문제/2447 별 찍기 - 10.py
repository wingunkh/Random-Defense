def func(n):
    if n == 3:
        return ["***", "* *", "***"]
    
    stars = func(n // 3)
    result = []
    
    for row in stars:
        result.append(row * 3)
        
    for row in stars:
        result.append(row + ' ' * (n // 3) + row)
        
    for row in stars:
        result.append(row * 3)
        
    return result

n = int(input())

print("\n".join(func(n)))
