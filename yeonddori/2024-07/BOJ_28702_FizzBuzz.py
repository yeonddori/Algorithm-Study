for i in range(3, 0, -1):
    x = input()
    if x.isdigit():
        result = int(x) + i
        break

if result % 15 == 0:
    print("FizzBuzz")
elif result % 3 == 0:
    print("Fizz")
elif result % 5 == 0:
    print("Buzz")
else:
    print(result)
