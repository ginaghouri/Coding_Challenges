def print_first_then_first_half_then_say_hi_100(items):
    print(items[0])
    middle_index = len(items) // 2
    index = 0
    while index <= middle_index:
        print(items[index])
        index += 1
    for time in range(100):
        print("hi")
        
list1 = [1,2,3,4,5,6,7,8,9]
print_first_then_first_half_then_say_hi_100(list1)