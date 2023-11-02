def listduplicateremover(a_list):
    result_list = []    
    
    for item in a_list:
        if item not in result_list:
            result_list.append(item)
    return result_list

def setsduplicateremover(a_list):
    result_list = list(set(a_list))
    return result_list

list1 = [1,2,3,4,4,3,2,1]
print(f"List version: {listduplicateremover(list1)} set version: {setsduplicateremover(list1)}")