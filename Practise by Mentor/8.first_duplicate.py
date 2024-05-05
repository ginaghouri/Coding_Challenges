# Given a list of int between 1 and n, where n is the length of the list, write a function that returns
# the first int that appears more than once (when we read the list left to right)
# If no integer appears more than once, then we return -1.

list1 = [2,1,5,3,4]

def firstDuplicate(numbers):
    numbers_set = set()
    for number in numbers:
        if number in numbers_set:
            return number # if a duplicte is found, this loop will automatically end here with the 'return'
        else:
            numbers_set.add(number) # add() is for sets, append() is for lists
    
    return 'No duplicate'
    
print(firstDuplicate(list1))