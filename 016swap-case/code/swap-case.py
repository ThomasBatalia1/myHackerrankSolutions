def swap_case(s):
    reverse_word = []
    for i in s: #loops through word and stores letter with flipped capitalization
        reverse_word += i.swapcase() #using the swapcase function
    string = "" #string for storing final string with swapped case
    for j in reverse_word: #combines each swapped character to form final answer
        string += str(j)
    return string # returns final answer

if __name__ == '__main__':
