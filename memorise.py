# Given an array of integers, find the sum of its elements.

def simpleArraySum(ar):
       return sum (ar)



# Alice& Bob: compare triplets 

def compareTriplets(a, b):
    
    tap = 0 # total alice points
    tbp = 0 # total bob points
    
    # write code below this line
    for i in range(0, 3):
        if a[i]> b [i]:
            tap = tap+1
        elif a [i] < b [i]:
            tbp = tbp+1 
    
    return [tap, tbp]

# VeryBigNumber: return sum of array 

def aVeryBigSum(ar):
    return sum(ar)


# Finding the diagonal difference of a 3 rows - 3 columns matrix

def diagonalDifference(arr):

    left_sum = 0
    right_sum = 0

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            
            # we already wrote for the left diognal
            # we catch the elements where i == j
            # and add their value to left_sum
            if i == j: 
                left_sum += arr[i][j]
                
            # now lets filter the elements for right diagonal
            MAX = len(arr) - 1
            # We don't need to check for i, since i is already 0, 1, 2, 3
            # they probbly won't ask these
            # it was not too difficullt but still a bit advanced
            if j == MAX - i:
                right_sum += arr[i][j]

    # you used in in this
    # absolute - makes a -ve value positive
    difference = abs(left_sum - right_sum)
    
    return difference

"""
Indexes of a 4 rows, 4 columns matrix:

(0, 0)  (0, 1)  (0, 2)  (0, 3)
(1, 0)  (1, 1)  (1, 2)  (1, 3)
(2, 0)  (2, 1)  (2, 2)  (2, 3)
(3, 0)  (3, 1)  (3, 2)  (3, 3)

The index of each element ^ at their places

Now note the indexes
If we use a general term (i, j) to represent each term.

Consider 'left diognal': (0, 0) (1, 1) (2, 2) (3, 3)
So it means in the left diognal, i is equal to j
0 == 0
1 == 1
2 == 2
3 == 3

So we loop through all the elements: (0, 0)  (0, 1)  (0, 2)  (0, 3) (1, 0)  (1, 1)  (1, 2)  (1, 3) (2, 0)  (2, 1)  (2, 2)  (2, 3) (3, 0)  (3, 1)  (3, 2)  (3, 3)

And wherever i is equal to j, we add it's value to "left_sum"

Now lets find a pattern for right diognal

(0, 0)  (0, 1)  (0, 2)  (0, 3)
(1, 0)  (1, 1)  (1, 2)  (1, 3)
(2, 0)  (2, 1)  (2, 2)  (2, 3)
(3, 0)  (3, 1)  (3, 2)  (3, 3)

Note: 4 terms, so length is 4, but the MAX "INDEX" is 3, index of the last element is always LENGTH - 1

i is increasing every term by 1
j is decreasing every term by 1, starts from MAX index
in this case MAX is 3

Right-diognal: 

(0, 3)
(1, 2) 
(2, 1) 
(3, 0)
Look now
i is increasing by 1
j is decreasing by 1

so this information is very useful

for i in range(len(arr[0])):

in this loop 'i' starts from 0


(i, MAX - i) - general term for right diagonal
lets look
(0, 3)
(1, 2) 
(2, 1) 
(3, 0)

MAX index is equal to the LENGTH of the array minus 1
Minus is because indexes start from 0

so MAX = length - 1

(i, MAX - i) 

i = 0, 1, 2, 3
Now go through each term one by one
(i, MAX minus i)
The first value of i is 0
(i, MAX minus i) is the general term
so first
(0, MAX minus 0) -> what does it become? (0,3) WHAT IS THE VALUE OF MAX? i can't hear anything
yes

now what is the second term
(1, 3-1) = (1, 2)

third term:
(2, 3-2) = (2, 1)

fourth term
(3, 3-3) = (3, 0)

now lets put the terms together
(0,3) (1, 2) (2, 1) (3, 0)
lets see . is it correcT?
(0, 3)
(1, 2) 
(2, 1) 
(3, 0)

yes, they're the same
so the general term is: (i, MAX - i)
(0, 3)
(1, 2) 
(2, 1) 
(3, 0)
Look now
i is increasing by 1
j is decreasing by 1

so this information is very useful

for i in range(len(arr[0])):

in this loop 'i' starts from 0


(i, MAX - i) - general term for right diagonal
lets look
(0, 3)
(1, 2) 
(2, 1) 
(3, 0)

MAX index is equal to the LENGTH of the array minus 1
Minus is because indexes start from 0

so MAX = length - 1

(i, MAX - i) 

i = 0, 1, 2, 3
Now go through each term one by one
(i, MAX minus i)
The first value of i is 0
(i, MAX minus i) is the general term
so first
(0, MAX minus 0) -> what does it become? (0,3) WHAT IS THE VALUE OF MAX? i can't hear anything
yes

now what is the second term
(1, 3-1) = (1, 2)

third term:
(2, 3-2) = (2, 1)

fourth term
(3, 3-3) = (3, 0)

now lets put the terms together
(0,3) (1, 2) (2, 1) (3, 0)
lets see . is it correcT?
(0, 3)
(1, 2) 
(2, 1) 
(3, 0)

yes, they're the same
so the general term is: (i, MAX - i)

"""

# Workshop 1.1 Remove duplicates, return uniques of an array.

def remove_duplicates(arr):
    return list(set(arr))

#1.2 Find the largest number 
# arr or num , it's the same, yes
def find_largest_numbers(numbers):
    return max(numbers)

#1.3 
# count of appearance of numbers 
numbers = [1, 2, 3, 4, 1, 2, 3, 1, 3, 3, 2, 1, 6, 2, 4, 1, 5, 8, 3]
def count_numbers(nums):
    # 1. Create an empty dictionary
    # 2. Loop through the SET of array (converting to set is important to eliminate duplicates so it will go through each number only once)
    # 3. For every number , create a new 'key' in the dictionary equal to that number (i) , and the VALUE of that KEY should be set the 'count'
    # We can find how many times a number appears in a list using the the .count method. So count[i] = nums.count(i) works perfectly
    # this is it for today
    count = {}
    for i in range(set(nums)): 
        count[i] = nums.count(i)
    return count


#1.4
# numbers between 1 and 100 that are divisible by 3 and 5
# not even, for even we use number % 2 == 0
result = [i for i in range(1, 101) if i % 3 == 0 and i % 5 == 0]

#1.5 create a list 1 to 10 and their square numbers 

result = { i:i*i for i in range(1, 11) }

