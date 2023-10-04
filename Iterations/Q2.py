num = int(input("Please enter an integer greater than 0: "))

factors = []
for i in range(1, num):
    if num % i == 0:
        factors.append(i)



print(f"The integer is {num} and its factors are {factors}")