### Problem Statement
'''
Function that takes a array of integer and returns its powerset
Ex : array = [1,2,3]
     powerSet = [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]

'''

### Solution - 1
## Time -  O(n* 2^n)   | Space - O(n* 2^n) 
def powerSet(array):
    subsets = [[]]
    for ele in array:
        for i in range(len(subsets)):
            currentSubset = subsets[i]
            subsets.append(currentSubset + [ele])
    return subsets


### Solution - 2
## Time -  O(n* 2^n)   | Space - O(n* 2^n) 

def powerSet2(array,idx=None):

    if idx is None:
        idx = len(array)-1
    elif idx < 0:
        return [[]]
    ele = array[idx]
    subsets = powerSet2(array,idx-1)
    for i in range(len(subsets)):
        currentSets = subsets[i]
        subsets.append(currentSets + [ele])
    return subsets


print(powerSet2([1,2,3]))


