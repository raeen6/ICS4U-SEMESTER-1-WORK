def unique(a_list):
    b_list = []

    for item in a_list:
        for char in item:
            b_list.append(char)
    
    final_set = set(b_list) 
    
    return final_set

a_list = ["apple", "banana", "cherry", "date"]

print(f"The unqiue characters in the list {a_list} are {unique(a_list)}")