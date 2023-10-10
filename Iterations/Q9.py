num1 = int(input('Enter num1: '))
num2 = int(input('Enter num2: '))

upper_limit = min(num1, num2)

for divider in range(1, upper_limit+1):
    if num1 % divider == 0 and num2 % divider == 0:
        print(f'{num1} and {num2} share a factor of {divider}.')