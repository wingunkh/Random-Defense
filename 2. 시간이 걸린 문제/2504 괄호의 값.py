s = input()
stack = []
tmp = 1
result = 0

for i in range(len(s)):
    k = 1
    if s[i] == '(':
        stack.append(s[i])
        tmp *= 2
    elif s[i] == '[':     
        stack.append(s[i])
        tmp *= 3
    elif s[i] == ')':
        if not stack or stack[-1] == '[':
            result = 0
            break
        elif s[i - 1] == '(':
            result += tmp
            
        stack.pop()
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        elif s[i - 1] == '[':
            result += tmp
            
        stack.pop()
        tmp //= 3
        
if stack:
    print(0)
else:
    print(result)
