serviceCost = float(input("Enter the total cost of service provided by the company: "))
tip = int(input("Enter the percentage for the tip: "))
totalCost = serviceCost * (tip/100 + 1)
print(f"Here is the total cost: {totalCost}")