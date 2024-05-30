dic = {
    'A+': 4.5, 'A0': 4.0,
    'B+': 3.5, 'B0': 3.0,
    'C+': 2.5, 'C0': 2.0,
    'D+': 1.5, 'D0': 1.0,
    'F': 0.0
}
sum = 0
result = 0

for _ in range(20):
    buff = input().split()

    if buff[2] != 'P':
        sum += float(buff[1])
        result += float(buff[1]) * dic[buff[2]]

print(result / sum)
