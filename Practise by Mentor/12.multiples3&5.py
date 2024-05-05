# Basic Solution, Using a For Loop
# calsum1(3, 5, 100000000)
# Total time: 57.4767 s
def calsum1(a, b, n):
    return sum((i for i in range(n) if i % a == 0 or i % b == 0))

# Using Mathematics - EXTREMELY FAST!
# Passing an ridiculously large value still results in amazingly fast results.
# calsum2(3, 5, 1000000000000000000000000000000) 
# Total time: 1.09e-05 s
def calsum2(a, b, n):
    n -= 1
    c = a*b

    d1 = n // a
    d2 = n // b
    d3 = n // c

    r1 = a * d1 * (d1 + 1)
    r2 = b * d2 * (d2 + 1)
    r3 = c * d3 * (d3 + 1)

    return (r1 + r2 - r3) / 2

#Source: https://projecteuler.net/problem=1

#This is the first problem on Project Euler, which is quite easy to solve using a simple for loop.
#However I wanted to take it further.
#I tried deriving a formula to be able to solve it and after some time I was able to come up with
#a solution.
#There is a series summation formula which we study in high school n(n + 1) / 2 and this came in
#handy. I figured, we can find the value of n by dividing the "target" value by the number who's 
#series we are trying to calculate so it can be target / 3 or target / 5, or any other number. 
#After we get the value of n , we can calculate the summation and multiply the result 3 or 5. 
#It can basically get the sum of all the multiples of 3 or 5 up till n.
#I can then sum both of them up, however there would be a small problem - the duplicates, because
#there are obviously some common multiples between 3 and 5. After some searching, I was able to 
#figure out, I can eliminate the duplicates by subtracting the multiples of 3x5 (15) from the sum
#Using this information I wrote down the formula and tried simplifying it to reduce the number of
#operations, and I was able to have somewhat of an efficient solution as a result.
