numbers = [5, 3, 1, 5, 2, 7, 10, -1]

"""
1. Store the first index of the list in a container called largest.
2. Loop through rest of the elements of the list.
3. Compare the value of largest with the value of i (each element of the list).
4. If i is larger than largest then store the value of i in largest which is basically: largest = i
5. In the end, return largest
"""

largest = numbers [0]
for number in numbers:
    if number > largest:
        largest = number

print (largest)

# smallest= numbers [0]
# for number in numbers:
#     if number < smallest:
#         smallest = number

# print (smallest)

