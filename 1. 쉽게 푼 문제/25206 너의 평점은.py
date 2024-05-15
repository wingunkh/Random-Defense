def func(grade):
    if grade == "A+":
        return 4.5
    elif grade == "A0":
        return 4.0
    elif grade == "B+":
        return 3.5
    elif grade == "B0":
        return 3.0
    elif grade == "C+":
        return 2.5
    elif grade == "C0":
        return 2.0
    elif grade == "D+":
        return 1.5
    elif grade == "D0":
        return 1.0
    else:
        return 0.0

sum = 0
result = 0

for i in range(20):
    buff = input().split()
    
    if buff[2] == 'P':
        continue
    
    sum += float(buff[1])
    result += float(buff[1]) * func(buff[2])

print(result / sum)
