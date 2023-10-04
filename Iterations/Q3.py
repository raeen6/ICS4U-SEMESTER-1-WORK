num_checker = False

if num_checker = True: 
    num = int(input("Please enter an integer greater than 1: "))
    if num > 0:
        num_checker = True


prime = True

for i in range (2, num):
    if num % i == 0:
        prime = False
        break

if prime:
    print(f"The number {num} is a prime number")
else:
    print(f"The number {num} is not a prime number")