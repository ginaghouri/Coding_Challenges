# Convert the number to its opposite , for-example if n is 123, change it to 321. Also consider negative numbers so -123 should be -321 (not 321-)

def reversedNumber(n):
    # create variable and store the value as string
    number = str(n)
    
    if n >= 0:
        return number[::-1]
    else:
        return '-' + number[1:][::-1] #slice, reverse an add - manually
    
print(reversedNumber(-123))
