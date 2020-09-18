### Problem Statement
'''
Find the longest substring without duplicate characters in a string
Example : string = "abacdsjfwsdw"
          Answer = "bacdsjfw
'''

### Solution - 1
# Time - O(n^2)
# Space - O(n)
def longestSubstringWithoutDuplicates(string):
    longestSubstring = ""
    if len(string) < 2:
        return string
    for i in range(len(string)):
        dictLetters= {string[i]:1}
        for j in range(i+1,len(string)):
            if string[j] in dictLetters:
                j -= 1
                break
            else:
                dictLetters[string[j]] = 1
        if len(string[i:j+1]) > len(longestSubstring):
            longestSubstring = string[i:j+1]
    return longestSubstring


### Solution 2
# Time - O(n)
# Space - O(min(n,a)) - minimum of length of string(n) or number of unique letters in string(i.e., set(a))

def longestSubstringWithoutDuplicates1(string):
    startIdx = 0
    longest = [0,1]
    dictStrings = {}
    for index,letter in enumerate(string):
        if letter in dictStrings:
            startIdx = max(startIdx,dictStrings[letter]+1)    
        if longest[1] - longest[0] < (index+1-startIdx):
            longest = [startIdx,index+1]
        dictStrings[letter] = index
    return string[longest[0]:longest[1]]
    

string = "sajufgeui"
print(longestSubstringWithoutDuplicates1(string))