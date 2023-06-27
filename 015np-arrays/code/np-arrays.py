import numpy #imports the numpy library
#we need to reverse the array using numpy functionality from the online video module
def arrays(arr):
    # complete this function
    # use numpy.array
    reverse_array = arr[::-1] #uses numpy functionality to reverse the array
    return numpy.array(reverse_array,dtype='float') #returns the array with all entries as floats

arr = input().strip().split(' ')
