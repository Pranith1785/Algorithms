### Problem Statement
'''
Function that takes an array of unique integers and 
returns the array of all permutations of those integers
ex : array = [1,2,3]
     sol = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
'''


### Solution 1
## Time Complexity - O(n*n!) -  worst - O(n^2*n!)
## Space Complexity - O(n*n!)
def getPermutations(array):
     permutations = []
     permutationsHelper(array,[],permutations)
     return permutations

def permutationsHelper(array,current_Perm,permutations):

     if len(array)==0:
          permutations.append(current_Perm)
     else: 
          for i in range(len(array)):                     
               newArray = array[:i] + array[i+1:]
               new_permutations = current_Perm + [array[i]]
               permutationsHelper(newArray,new_permutations,permutations)


### Solution 2
## Time - O(n*n!)
## Space - O(n*n!)

def getPermutations1(array):
     permutations = []
     permutationsHelper1(0,array,permutations)
     return permutations

def permutationsHelper1(i,array,permutations):

     if i == len(array)-1:
          permutations.append(array[:])
     else:
          for j in range(i,len(array)):
               swap(array,i,j)
               permutationsHelper1(i+1,array,permutations)
               swap(array,i,j)

def swap(array,i,j):
     array[i],array[j] = array[j],array[i]


print(getPermutations1([1,2,3,4]))



    
