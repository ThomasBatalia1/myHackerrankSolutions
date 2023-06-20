def average(array):
    # your code goes here
    set_data =set(arr) #converts the given array into a set
    sum = 0 
    for i in set_data: #iterates through the set and adds all values to the sum
        sum += i
    sum = sum / len(set_data) #returns the average of the sum using the length of the set
        
    return round(sum,3)
if __name__ == '__main__':
