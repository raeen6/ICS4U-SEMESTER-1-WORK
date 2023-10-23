def if_anagram(arg1, arg2):
    ''' Returns True or False whether the 2 strings are anagrams or not
    
    arguements: 
        arg1: string1
        arg2: string2

    return:
        True or false based on whether arg1 and arg2 are anagrams
    '''
    text1 = list(arg1)
    text2 = list(arg2)

    arg1 = arg1.lower()
    arg2 = arg2.lower()


    if len(arg1) != len(arg2):
        return False

    for char in (text1):
        if char not in text2:
            return False

    return True

word1 = input("Please enter word1: ")
word2 = input("Please enter word2: ")

print(f"The words {word1} and {word2} being anagrams is {if_anagram(word1, word2)}")