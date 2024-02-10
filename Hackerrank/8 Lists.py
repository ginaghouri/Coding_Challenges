#Consider a list (list = []). You can perform the following commands:insert i e : 1.Insert integer e at position i 2.print : Print the list 3.remove e : Delete the first occurrence of integer e
#4.append e : Insert integer e at the end of the list 5.sort : Sort the list 6.pop : Pop the last element from the list 7.reverse : Reverse the list
#Pseudocode:
#N = int(input()) #number of commands, provided by tester
#print each item starting from 0 to N 

if __name__ == '__main__':
    N = int(input())
    the_list = list()

    for _ in range(N):
        query = input().split()
        if query[0] == "print":
            print(the_list)
        elif query[0] == "insert":
            the_list.insert(int(query[1]), int(query[2]))
        elif query[0] == "remove":
            the_list.remove(int(query[1]))
        elif query[0] == "append":
            the_list.append(int(query[1]))
        elif query[0] == "sort":
            the_list = sorted(the_list)
        elif query[0] == "pop":
            the_list.pop()
        elif query[0] == "reverse":
            the_list.reverse()