#nested loop

list1 = ['a',1,'z','abcdefg']
# its time complexity is O(N^2) because there is a loop inside a loop.
# for i in list1:
#     for j in list1:
#         print(i, j)
        
list2 = ['Maria', 'King', 'Herald', 'Ron', 'James', 'Queen']

for i in list2:
    for j in list2:
        if i != j:
            print(i + ' can pair up with ' + j)