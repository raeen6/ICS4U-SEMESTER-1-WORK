num = int(input("Please enter a number: "))
factor_list = [ ]

for divider in range(2, num+1):
    if num % divider == 0:
        is_prime = True
        for i in range(2, divider):
            if divider % i == 0:
                is_prime = False
                break
        if is_prime:
            factor_list.append(divider) 


if factor_list:
    largest_prime_factor = max(factor_list)
    print(f"The number {num} has prime factors of {factor_list} with the largest prime factor of {largest_prime_factor}")
else:  
    print("There are no prime factors")
