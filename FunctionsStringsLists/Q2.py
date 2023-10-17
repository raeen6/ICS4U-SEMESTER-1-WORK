def palindrome(arg1):
    ''' Says whether or not the string is a palindrome

    arguments:
        arg1 : represents the word input

    return: 
        whether or not the string is a palindrome
    
    '''
    size = len(arg1)
    word = ''
    for i in range(1, size+1):
        word += arg1[-i] 
    
    if word == arg1:
        return True
    else:
        return False
# end of palindrome()

word1 = input("Please enter a word: ")

print(f"The word {word1} being a palindrome is: {palindrome(word1)}")
