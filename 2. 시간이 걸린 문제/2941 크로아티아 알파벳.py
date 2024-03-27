s = input()
croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for i in croatia:
    s = s.replace(i, '?')
    # replace() 함수는 교체한 문자열을 반환

print(len(s))
