def swap_case(s): #defines the function for swap case
    reverse_word = [] #sets up array that will be the reversed word
    for i in s: #loops through word and stores letter with flipped capitalization
        reverse_word += i.swapcase() #using the swapcase function
    string = "" #string for storing final string with swapped case
    for j in reverse_word: #combines each swapped character to form final answer
        string += str(j)  #adds each entry in reverse_word in the string format to the string
    return string # returns final answer

if __name__ == '__main__':
