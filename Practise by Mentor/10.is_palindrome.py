# Check if the following string is a palindrome
test1 = "abcddcba"

# the function name should be "is_palindrome" and it should accept one argument called "my_string"
#is_palindrome true or false 
# Step 1: Find the half length of the string (ensure that it's an integer value)
# Step 2: Create a for loop using that half length, syntax => for i in range(half_length):
# Step 3: Every iteration, compare the last and the first element, and then narrow down the closer elements
# Hint for step 3: it will represent the index, so my_string[i] will give you elements from the start, my_string[-(i + 1)] will give you elements from the end
# Compare the first and last corresponding letters and if any of them not equal then it's not equal then it's not a palindrome
# If the loop finishes successfully then it's a palindrome

def is_palindrome (my_string):
    half_length = int (len (my_string) // 2)

    for i in range (half_length):
        if my_string [i] != my_string [-(i + 1)]:
            return False 
    return True 

print(is_palindrome("abcddcb"))