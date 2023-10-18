def constanantctr(arg1):
    ''' Counts amount of constanants in a word

    arguments: 
        arg1: represents the word input

    return:
        Amount of constonants in a word
    '''
    ctr = 0
    for character in (arg1):
        if character.lower() not in "aeiou":
            ctr += 1

    return ctr
def vowelctr(arg1):
    ''' Counts amount of vowels in a word

    arguments: 
        arg: represents the word input

    return:
        Amount of vowels in a word
    '''
    ctr = 0
    for character in (arg1):
        if character.lower() in "aeiou":
            ctr += 1
    return ctr

word = input("Please input a word: ")

print(f"The word {word} has {constanantctr(word)} constanants")
print(f"The word {word} has {vowelctr(word)} vowels")