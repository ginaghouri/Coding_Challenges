    
   #Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.

    # Given input is the 'arr' list, it contains all the scores
    # 1. Remove Duplicates
    # - Convert 'arr' into a set
    # - Convert 'arr' back into a list
    
    # 2. Sort
    # - Simple sorted() function , or .sort() method
    # 3. Print the 2nd element of 'arr' 
    
    # Converting 'arr' to set and storing it back into 'arr'
   arr = set(arr)
    
    # Now, Converting 'arr' back to list, and storing in itself
    arr = list(arr)
    
    # Sorting 'arr'
    arr.sort()
    
    # Printing 2nd last element (because it sorts in ascending order)
    print(arr[-2])

    # Notes:
    # Converting a list into a set removes all the duplicates because the property of a set is that it can only contain unique elements
    # So using this property, we convert the list into a set, it removes all duplicates, then we convert back into a list. 
    # We convert back into a list because set is an unordered structure, there is no order in a set, so it cannot be sorted.
    # A list has an order, every element has a fixed position, thats why we can access elements using indexing: listName[0] etc.
    # A shorter way is to do this whole process in 1 line
    # So here is a shorter version of the solution:
    arr = list(set(arr)) # this line converts arr into a set then converts back to list
    arr.sort()
    print(arr[-2])

    # We can use the sorted() function instead of the .sort() method to make it even shorter, since sorted() directly returns the sorted list instead of modifying the original
    # So here is the solution in 1 line:
    print(sorted(list(set(arr)))[-2])