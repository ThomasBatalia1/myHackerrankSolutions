if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    #variables for our sum
    sum = 0
    
    #for loop for our specific student
    for j in student_marks[query_name]:
        #adds each individual grade to our sum
        sum += j
    
    #finds average
    result = sum/(len(student_marks[query_name]))   

    #uses for string to properly print result with 2 points after decimal
    print('%.2f' % result)
        
           
    
      
