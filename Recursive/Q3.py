def palin(word):

    if len(word) <= 1:
        return True
        
    elif word[0] == word[-1]:
        return palin(word[1:-1])

    else:
        return False


word = "tacocat"
print(palin(word))