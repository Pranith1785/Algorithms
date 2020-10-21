### Problem Statement
'''
Function that takes two strings and 
returns the minimum number of operations to be done on first string to obtain the second string
Input : string1 = "abc"
        string2 = "xabd"
Ouptut : Ans : 2 (add 'x' and replace 'c' with 'd')
'''

### Solution 1
##Time - O(nm) -- lengths of strings 'n' and 'm' 
## space - O(nm)
def levenshteinDistance(string1,string2):
    editMatrix = [[x for x in range(len(string1)+1)] for y in range(len(string2)+1)]
    for i in range(1,len(string2)+1):
        editMatrix[i][0] = 1 + editMatrix[i-1][0]
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if string1[i-1] == string2[j-1]:
                editMatrix[j][i] = editMatrix[j-1][i-1]
            else:
                editMatrix[j][i] = 1 + min(editMatrix[j-1][i],editMatrix[j-1][i-1] ,editMatrix[j][i-1])
    return editMatrix[-1][-1]

print(levenshteinDistance("","safjkfsak"))

