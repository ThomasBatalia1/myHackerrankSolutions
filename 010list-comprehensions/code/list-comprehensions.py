if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    possible_permutations = [[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1)] #returns a list of lists with all the possible permutations of the three data points
    
Results = [i for i in possible_permutations if sum(i) != n] 
#this goes through our possible permutation and stores the value to results, only if sum does not equal n.
print(Results) #prints the results as requested
