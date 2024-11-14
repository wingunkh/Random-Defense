a = list(input())
stack = []
tmp = 1
result = 0

for i in range(len(a)):
    if a[i] == '(':
        stack.append(a[i])
        tmp *= 2
    elif a[i] == '[':
        stack.append(a[i])
        tmp *= 3
    elif a[i] == ')':
        if stack and stack.pop() == '(':
            if a[i - 1] == '(':
                result += tmp

            tmp //= 2
        else:
            result = 0
            break
    elif a[i] == ']':
        if stack and stack.pop() == '[':
            if a[i - 1] == '[':
                result += tmp
                
            tmp //= 3
        else:
            result = 0
            break
else:
    if stack:
        result = 0

print(result)
