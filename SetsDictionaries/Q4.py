def dictreverse(a_dict):

    result_dict = {}
    for key, value in a_dict.items():
        result_dict[value] = key
    return result_dict


example_dict = {
    'g':2,
    'b':3 
}
print(dictreverse(example_dict))