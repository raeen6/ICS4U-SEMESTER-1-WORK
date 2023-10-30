from random import randrange

def rand_list(start, end, frequency):
    if start < end and frequency > 0:
        list1 = []
        for _ in range(frequency):
            new_value = randrange(start, end+1)
            list1.append(new_value)
        return list1
    else:
        return []

print(rand_list(1,1000,30))