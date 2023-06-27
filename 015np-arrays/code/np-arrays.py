import numpy #imports the numpy library

def arrays(arr):
    # complete this function
    # use numpy.array
    reverse_array = arr[::-1] #uses numpy functionality to reverse the array
    return numpy.array(reverse_array,dtype='float') #returns the array with all entries as floats

arr = input().strip().split(' ')
