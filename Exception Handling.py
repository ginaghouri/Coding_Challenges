#Exception handling: allows to handle errors that may occur during the execution of code. 
#It helps to prevent program from crashing and allows to take appropriate actions when an error occurs. 
#Exceptions are raised when errors occur during the program's execution, and they can be caught and handled using try, except, else, and finally blocks.

try:
    # Code that may raise an exception
    result = 10 / 0  # This will raise a ZeroDivisionError
except ZeroDivisionError:
    # Handle the specific exception
    print("Error: Cannot divide by zero!")
except Exception as e:
    # Handle other exceptions
    print(f"An error occurred: {e}")
else:
    # This block is executed if no exceptions occur in the try block
    print("No errors occurred.")
finally:
    # This block is always executed, whether an exception occurred or not
    print("Finally block executed.")


#Try block: Contains the code that may raise an exception.
#Except block: Catches and handles specific exceptions. You can have multiple except blocks to handle different types of exceptions.
#Example 1: Handling ZeroDivisionError  
    
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

#Example 2: Handling FileNotFoundError   
    
try:
    with open("nonexistent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found!")
except Exception as e:
    print(f"An error occurred: {e}")

#Else block (optional): Executed if no exceptions occur in the try block.
    
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")

#Finally block (optional): Always executed, regardless of whether an exception occurred or not.
    
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
else:
    print(f"Result: {result}")
finally:
    print("Finally block executed.")
