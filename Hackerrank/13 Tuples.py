#Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':

    n = int(input())
    integer_list = map(int, input().split())
    my_tuple = tuple(integer_list)
    result = hash(my_tuple)
    print(result)

