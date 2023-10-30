def stringtolist(string1):  

    string2 = string1.split(',')
    resultlist = []

    for char in string2:
        resultlist.append(int(char))

    return resultlist

numbers = input("Please enter numbers: ")

print(f"The list and integer version of your numbers are: {stringtolist(numbers)}")


