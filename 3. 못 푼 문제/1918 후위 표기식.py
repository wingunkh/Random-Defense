s = list(input())
stack = [] # 괄호 또는 연산자만 삽입하는 스택
result = ""

for i in range(len(s)):
    if s[i] == '(':
        stack.append(s[i])
    elif s[i] == ')': # 닫는 괄호일 경우
        while stack and stack[-1] != '(':
            result += stack.pop() # 괄호 내부의 모든 연산자 정답에 추가

        stack.pop() # 여는 괄호 제거
    elif s[i] == '+' or s[i] == '-': # + 또는 -일 경우
        while stack and stack[-1] != '(':
            result += stack.pop() # 괄호 내부의 모든 연산자 정답에 추가

        stack.append(s[i])
    elif s[i] == '*' or s[i] == '/': # * 또는 /일 경우
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result += stack.pop() # 괄호 내부의 * 또는 /만 정답에 추가

        stack.append(s[i])
    else: # 알파벳일 경우
        result += s[i]

while stack:
    result += stack.pop()

print(result)
