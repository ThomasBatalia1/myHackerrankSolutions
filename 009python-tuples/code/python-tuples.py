# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
str_input = sys.stdin.read() #reads the data from STDIN
tuple = ()
split_data = str_input.split("\n") #Splits the input into two strings First one is total number of entries, second one is the data
data = split_data[1].split(" ") #splits our data into a series of strings
for i in data:
    tuple += (int(i),) # for each data point it converts the value to a int, then adds a tuple of length 1 to our original tuple variable
print(hash(tuple)) #this will not return the correct hash value on the hackerrank website due to a difference in hashing algorithm, but does return the correct tuple.

# same as last semester :)
