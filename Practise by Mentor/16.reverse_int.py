def reverseInt(n):
    str_integer = str(n)
    if str_integer[0] == '-':
        print('-' + str_integer[:0:-1])
    else:
        print(str_integer[::-1])
    
reverseInt(-15)