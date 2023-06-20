if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    arr = list(arr) #turns array into a list
    
    arr.sort(reverse=True) #sorts the array from smallest to largest number
    
    i = 1 #second largest would be in index 1, unless there is a repeated max
    while(arr[i] == arr[i-1]): #checks if second position is equal to first, if it is, moves the index over by one
        i = i+1
    
    print(arr[i]) #returns the second largest number
        
    
