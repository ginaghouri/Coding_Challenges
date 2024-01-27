# 1.Given an array of integers, find the sum of its elements.

def simpleArraySum(ar):
       return sum (ar)



# 2.Alice& Bob: compare triplets 

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

# 3.VeryBigNumber: return sum of array 

def aVeryBigSum(ar):
    return sum(ar)


# 4.Finding the diagonal difference of a 3 rows - 3 columns matrix

def diagonalDifference(arr):

    left_sum = 0
    right_sum = 0

    for i in range(len(arr[0])):
        for j in range(len(arr)):
            
            # we already wrote for the left diagonal
            # we catch the elements where i == j
            # and add their value to left_sum
            if i == j: 
                left_sum += arr[i][j]
                
            # now lets filter the elements for right diagonal
            MAX = len(arr) - 1
            # We don't need to check for i, since i is already 0, 1, 2, 3

            if j == MAX - i:
                right_sum += arr[i][j]

    # absolute - makes a negative value positive
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

Consider 'left diagonal': (0, 0) (1, 1) (2, 2) (3, 3)
So it means in the left diagonal, i is equal to j
0 == 0
1 == 1
2 == 2
3 == 3

So we loop through all the elements: (0, 0)  (0, 1)  (0, 2)  (0, 3) (1, 0)  (1, 1)  (1, 2)  (1, 3) (2, 0)  (2, 1)  (2, 2)  (2, 3) (3, 0)  (3, 1)  (3, 2)  (3, 3)

And wherever i is equal to j, we add it's value to "left_sum"

Now lets find a pattern for right diagonal

(0, 0)  (0, 1)  (0, 2)  (0, 3)
(1, 0)  (1, 1)  (1, 2)  (1, 3)
(2, 0)  (2, 1)  (2, 2)  (2, 3)
(3, 0)  (3, 1)  (3, 2)  (3, 3)

Note: 4 terms, so length is 4, but the MAX "INDEX" is 3, index of the last element is always LENGTH - 1

i is increasing every term by 1
j is decreasing every term by 1, starts from MAX index
in this case MAX is 3

Right-diagonal: 

(0, 3)
(1, 2) 
(2, 1) 
(3, 0)
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
(0, MAX minus 0) -> what does it become? (0,3) WHAT IS THE VALUE OF MAX?

now what is the second term:
(1, 3-1) = (1, 2)

third term:
(2, 3-2) = (2, 1)

fourth term:
(3, 3-3) = (3, 0)

now lets put the terms together
(0,3) (1, 2) (2, 1) (3, 0)
lets see . is it correct?
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


