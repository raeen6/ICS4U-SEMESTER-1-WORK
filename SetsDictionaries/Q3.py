def i_count(a_list):
    ''' function made to grab elements that are common to all sets.

    Argument:  
        a_list: multiple sets

    Return:
        Int: Returns elements that are common to all sets.
    '''
    if a_list:
        result_set = a_list[0]

        for example_set in a_list[1:]:
            result_set = result_set & example_set

        return len(result_set)

test = [{1,2,3,7}, {3,4,5,7}, {5,6,7,8}]
print(i_count(test))