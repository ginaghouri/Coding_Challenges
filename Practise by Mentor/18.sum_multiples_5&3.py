
def sum_multiples_3_5(num_limit):
    total = 0
    for value in range(num_limit):
        if value % 3 == 0 or value % 5 == 0:
            total += value
        # elif value % 5 == 0:
        #     total += value
    return total

print(sum_multiples_3_5(1000))