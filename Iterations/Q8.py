name = " "

longest_name = " "
longest_length = 0

while name != 'X':
    name = input("Enter your name or 'X' to exit.: ")

    if name != 'X':
        current_length = len(name)

        if current_length > longest_length:
            longest_length = current_length
            longest_name = name
else:
    print("End of the inputs.")

if longest_name:
    print(f"The longest name with {longest_length} characters is {longest_name}")
else:
    print("Not enough data")