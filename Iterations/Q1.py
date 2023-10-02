# While Loop Calculator
num = int(input())
total_product = 1
num2 = num

while num != 0:
    total_product *= num
    num -= 1

print(f"Factorial of {num2} is {total_product}")

# For Loop Calculator
total_product2 = 1

for i in range(num2, 0, -1):
    total_product2 *= i
print(f"Factorial of {num2} is {total_product2}")