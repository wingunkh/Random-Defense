a = [input() for _ in range(3)]
target = 0

for i in range(3):
    if a[i] not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(a[i]) + (3 - i)
        break

if n % 15 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)
