def duplicate_finder(arg1, arg2):
    ''' Finds characters found in both of 2 string inputs

    Arguments
        arg1: input 1
        arg2: input 2

    return:
        Returns a list of the characters that were found in both strings
    '''
    text = []

    arg1 = arg1.lower()
    arg2 = arg2.lower()

    for char in arg1:
        if char in arg2:
            text.append(char)
            
    text.sort()

    return text

word1 = input("Please enter word1: ")
word2 = input("Please enter word2: ")

print(f"The two words of {word1} and {word2} have the same letters of {duplicate_finder(word1, word2)}")