### Problem Statement
'''
Function that returns the index of string's first non-repeating character.
If string doesnt have any non-repeating character return -1

Example : string = "abcdaed"
          Ans  = 1 ('b' is not repeated)
'''

### Solution -1
## Time - O(N^2) | Space - O(1)
def firstNonRepeatCharacter(string):

    for i in range(len(string)):
        value = string[i]
        foundDuplicate = False
        for j in range(len(string)):
            if value == string[j] and i != j:
                foundDuplicate = True
        if not foundDuplicate:
            return i
    return -1 

### Solution - 2
## Time - O(N) | Space - O(1) -  here we are create dict for small case alphabets and will not be more than 26 keys 

def firstNonRepeatCharacter2(string):

    countDict = {}
    for ele in string:
        countDict[ele] = countDict.get(ele,0) + 1
    
    for idx, ele in enumerate(string):
        if countDict[ele] == 1 :
            return idx
    return -1



print(firstNonRepeatCharacter2("faadabcbbebdf"))
