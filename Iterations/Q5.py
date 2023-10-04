N = int(input("Please enter a number greater than 1: "))


ctr = 0
result_num = 0
for num in range(1, N+1):
    total_factors = 0
    for divider in range(1, num+1):
        if num % divider == 0:
            total_factors += 1
    if total_factors > ctr:
        ctr = total_factors
        result_num = num

print(f"The number {result_num} has the most factors of {total_factors} from the range of 1 to {N}")
