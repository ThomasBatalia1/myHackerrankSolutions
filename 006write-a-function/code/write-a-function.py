def is_leap(year):
    leap = False
    if ((year % 4) == 0): #checks if number is divisible by 4
        leap = True
    if((year % 100) == 0): #checks if number is divisible by 100
        leap = False
        if((year % 400) == 0): #checks if number is divisible by 400, this block is only ran if the number was also divisible by 100
            leap = True 
        
    return leap

year = int(input())
