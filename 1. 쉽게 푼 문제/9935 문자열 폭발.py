s = list(input())
bomb = list(input())
stack = []

for i in s:
    stack.append(i)
    
    if stack[-len(bomb):] == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if stack:
    print(''.join(map(str, stack)))
else:
    print("FRULA")
