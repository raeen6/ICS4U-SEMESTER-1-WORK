num = int(input("Enter an integer greater than -1: "))

fib_0 = 0
fib_1 = 1
fib_n = 0

for _ in range(2, num+1):
    fib_n = fib_0 + fib_1

    fib_0 = fib_1
    fib_1 = fib_n

print(f"The fibnoacci number of {num} is {fib_n}")

