def expo(base, power):
    if base == 0:
        return 0
    elif base == 1:
        return power
    else:
        return power * expo(base - 1, power)

print(expo(2,4))

