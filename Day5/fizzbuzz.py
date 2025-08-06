for angka in range(1,101):
    if (angka % 3 == 0 and angka % 5 == 0):
        print("FizzBuzz")
    elif angka % 3 == 0:
        print("Fizz")
    elif angka % 5 == 0:
        print("Buzz")
    else:
        print(angka)