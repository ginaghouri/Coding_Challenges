numbers = [5, 2, 3, -1, 21, 92]
length = len(numbers)

total = 0
for i in range(length):
    total = total + numbers[i]
    
print(total)

# Analogy
# s ~ total
# n ~ length
# f(i) ~ numbers[i]

numbers = [5, 2, 3, -1, 21, 92, 4, 6, 2, 1, 52, 53]
length = len(numbers)

# sum all the ODD numbers
total = 0
for i in range(length):
    if numbers[i] % 2 != 0:
        total = total + numbers[i]

print(total)

# Analogy
# s ~ total
# n ~ length
# cond(i) ~ numbers[i] % 2 != 0
# f(i) ~ numbers[i]
