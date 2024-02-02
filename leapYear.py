"""
https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.
"""

def is_leap(year):
    if year % 4 != 0:
        return False
    
    elif year % 4 ==0 and year % 100!=0 and year % 400!=0:
        return True
    elif year % 4== 0 and year % 100 != 0 and year % 400==0:
        return True
    elif year % 4 ==0 and year % 100 == 0 and year % 400!= 0:
        return False 
    elif year % 4 == 0 and year % 100 ==0 and year % 400 ==0:
        return True  
    
    
    

year = int(input())
print(is_leap(year))
