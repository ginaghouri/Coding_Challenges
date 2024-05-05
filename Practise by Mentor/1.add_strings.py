# 14 = 10 + 4 = (10^1 * 1) + (10^0 * 4)

# 22 = 20 + 2 = (10^1 * 2) + (10^0 * 2)

# 153 = 100 + 50 + 3 = (10^2 * 1) + (10^1 * 5) + (10^0 * 3)

# 234 = 200 + 30 + 4 = (10^2 * 2) + (10^1 * 3) + (10^0 * 4)

# 5423 = 5000 + 400 + 20 + 3 = (10^3 * 5) + (10^2 * 4) + (10^1 * 2) + (10^0 * 3)

# 351 = 1*10^0 + 5*10^1 + 3*10^2


# int()
# 6423
# print((3 * 10**0) + (2 * 10**1) + (4 * 10**2) + (6 * 10**3))

def toInt(number):
    index = 0
    final_number = 0
    for digit in number[::-1]:
        value = ord(digit) - 48
        final_number += value * 10**index
        index += 1
    return final_number
    
def strSum(num1, num2):
    return toInt(num1) + toInt(num2)
    
print(strSum('14', '22'))

