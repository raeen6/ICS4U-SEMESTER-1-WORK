def create_line(arg1):
    ''' Returns a string of 1 and 0 based on that argument

    argument:
        arg1: integer, to determine the length of the string

    return:
        text: series of 1 or 0 as a string
    
    '''
    
    text = ' '
    for i in range(1, arg1+1):
        if i % 2 == 0:
            text += '0'
        else:
            text += '1'
    return text

def output_pattern(arg1):
    for i in range(1, arg1+1):
        print(create_line(i))

x = output_pattern(5)

print(x)