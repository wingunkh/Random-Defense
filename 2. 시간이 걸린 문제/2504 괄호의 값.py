s = input()
stack = []
tmp = 1
result = 0

for i in range(len(s)):
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
        
        stack.pop()
        
        if s[i - 1] == '(':
            result += tmp
            
        tmp //= 2
    else:
        if not stack or stack[-1] == '(':
            result = 0
            break
        
        stack.pop()
        
        if s[i - 1] == '[':
            result += tmp
            
        tmp //= 3
else:
    if stack:
        result = 0

print(result)
