def mean(a_list):
    ''' total calulation of the total average from a given list of integers

    arg:
        a_list: list of integers

    return:
        int: The calculated average

    '''
    return sum(a_list) / len(a_list)

def median(a_list):
    ''' the middle most value in a given sorted list of integers

    arg:
        a_list: list of integers

    return:
        int: the middlemost value (or average of the middle two values)
    '''
    sorted_a_list = sorted(a_list)
    middle = len(a_list) // 2

    if len(a_list) % 2 == 0:
        left = sorted_a_list[middle-1]
        right = sorted_a_list[middle]
        return (left+right) / 2
    else:
        return sorted_a_list[middle]


from random import seed
from random import randrange

seed(1)
data = [randrange(1,100) for _ in range(randrange(10,30))] # list comprehension
print(f"Our random dataset: {data}")
print(f"Mean of our dataset: {mean(data)}")
print(f"Median of our dataset: {median(data)}")
