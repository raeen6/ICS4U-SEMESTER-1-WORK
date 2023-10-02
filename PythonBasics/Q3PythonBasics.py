num = int(input("Enter an integer: "))
if num % 2 == 0:
    print(f"{num} Has a remainder of 0 when divided by 2")
elif num % 2 == 1:
    print(f"{num} Has a remainder of 1 when divided by 2")
else:
    print(f"{num} Does not have a remainder of 0 or 1 when divided by 2")