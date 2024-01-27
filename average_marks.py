#The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# student_marks contain key-value pairs
    # keys are student names, example: Mouiz
    # values are lists of marks: [100, 100, 100]
    # query_name is name of the student who's marks we want to access and calculate the average of
    
    marksList = student_marks[query_name]
    average = sum(marksList) / len(marksList)
    
    print("%.2f" % average)
    