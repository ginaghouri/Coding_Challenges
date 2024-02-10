if __name__ == '__main__':
    n = int(input().strip())
    #Pseudocode:
    # A number is even if it's remainder when divided by 2 is equal to 0
    # A number is odd if it's remainder when divided by 2 is equal to 1
    # The remainder operator % is used
    # The remainder of 5 divided by 6 can be found out by 5 % 6
    
    #if n is odd:
    if n % 2 == 1:
        print('Weird')
    else:
        if n in range(2, 6) or n > 20:
            print('Not Weird')
        elif n in range(6, 21):
            print('Weird')
        