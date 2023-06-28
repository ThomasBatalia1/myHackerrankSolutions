def split_and_join(line): #defines the function for split and join
    
    line = line.split(" ") #splits the string into a array, seperates indexes at " "
    line = "-".join(line) #rejoins each index in the array with "-" between each.
    return line #returns the final string
if __name__ == '__main__':
