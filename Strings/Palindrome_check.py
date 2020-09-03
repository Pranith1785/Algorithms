### Problem Statement
'''
Check whether a string is Palindrome or not
'''

### Solution 1
#Time - O(n)
#Space - O(1)
def isPalindrome(strValue):

    left = 0
    right = len(strValue)-1
    while(left < right):
        if strValue[left] != strValue[right]:
            return False
        left += 1
        right -= 1
    return True

### Solution 2
#Time - O(n^2)  
#Space - O(n)
def isPalindrome2(strValue):
    newString = ""
    for i in range(len(strValue)-1,-1,-1):   ##for loop takes O(n) time
        newString += strValue[i]             ## string conact takes O(n) time
    
    return strValue == newString

### Solution 3
#Time - O(n)
#Space - O(n)
def isPalindrome3(strValue):
    '''using list '''
    newString = []
    for i in reversed(range(len(strValue))):   ##for loop takes O(n) time
        newString.append(strValue[i])          #list append takes O(1) time
    
    return strValue == "".join(newString)      ##join takes O(n) time


### Solution 4
# Time - O(n)
# Space - O(n)
def isPalindrome4(strValue,i=0):
    ''' recursive'''
    j = len(strValue)-1-i

    if i >= j:
        return True
    else:
        return strValue[i] == strValue[j] and isPalindrome4(strValue,i+1)


print(isPalindrome4("abcdcba"))