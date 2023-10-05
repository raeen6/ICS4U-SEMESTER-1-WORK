
n = int(input("How many marks do you have? "))

from statistics import mean 

loop = True

grades = []
while loop:
    for i in range(0, n):
        num = int(input("Please enter a number from 0 to 100: "))
        if num > 100 or num < 0:
            num = int(input("Please reenter a number FROM 0 to 100: "))
        grades.append(num)
    loop = False
    

average = mean(grades)

print(f"The average of your {n} marks is {average}% ")