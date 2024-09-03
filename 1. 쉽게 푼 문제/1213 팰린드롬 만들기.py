def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

stack = sorted(list(input()), reverse = True)
front = ""
back = ""
tmp = ""
result = ""

while stack:
    now = stack.pop()

    if now in stack:
        front += now
        back += stack.pop()
    else:
        tmp += now

result += front + tmp
result += back[::-1]

if is_palindrome(result):
    print(result)
else:
    print("I'm Sorry Hansoo")
