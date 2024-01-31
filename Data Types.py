#Python Data Types: provide a foundation for creating well-organized and flexible code in an object-oriented manner.
#Author: Gina Rubik

#1.Primitive Data Types: Integers, Floats, Booleans, Strings are basic building blocks of data.

num = 7
float_num = 3.14
boolean = True or False 
string = "Hello, World!"

#2.Composite Data Types: Lists, Tuples, Sets, and Dictionaries are used to store collections of data.

my_list = [1, 2, 3, 4]
my_tuple = (1, 2, 3)
my_set = {1, 2, 3}
my_dict = {'key': 'value', 'name': 'Mouiz'}

#3.Special Data Types: NoneType represents the absence of a value.

none_value = None

#4. Type Conversion: convert between different data types using functions like int(), float(), str(), etc.

num_str = "21"
num_int = int(num_str)       # Converts string to integer

def number_to_string(num):
    return str(num)          # str() function returns a string, it converts a number into a string

def string_to_number(s):     #functions transforms string to number and returns an integer
     return int(s) 

def boolean_to_string(b):    # converts Boolean value into its string representation
    return str (b)


