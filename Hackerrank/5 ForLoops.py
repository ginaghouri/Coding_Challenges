
#1. Write a program which prints numbers from 1 to 10. Use a for-loop to do this. Expected Output: 1 2 3 4 5 6 7 8 9 10

for i in range (1,11):

        print (i)

#2. Write a program which prints the square of all the numbers from 5 to 10. Use a for-loop to do this. Expected output: 25 36 49 64 81 100
   
for i in range(5, 11):
    
        print(i*i)

#3. Write a program which prints the squares of all the **even** numbers from 1 to 10. Use a for-loop to do this. Expected output: 4 16 36 64 100

for i in range(1, 11):
    if i % 2 == 0:
        print(i*i)


