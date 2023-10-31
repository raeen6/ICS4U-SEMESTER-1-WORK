def duplicateremover(a_list):
    result_list = []

    for item in a_list:
        if item not in result_list:
            result_list.append(item)

    return result_list

list1 = list(input("Please enter a list of characters: "))
print(f"This is the original version{list1} and this is the duplicate removed version{duplicateremover(list1)}")