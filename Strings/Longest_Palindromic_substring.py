### Problem Statement
'''
Find the longest palindrome substring from a given string
example : string = "abapqrqpxy"
          ans = "pqrqp"
'''

### Solution - 1
## Time - O(n^3)
## Space - O(1)
def longestPalindromicSubstring(string):
    palindromeString = ""
    for i in range(len(string)):
        for j in range(i,len(string)):
            subString = string[i:j+1]
            if len(palindromeString) < len(subString) and checkPalindrome(subString):
                palindromeString = subString
    return palindromeString

def checkPalindrome(string):
    left = 0
    right = len(string)-1
    while left < right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1       
    return True

### Solution - 2
## Approach: 
## 1. from every letter moving left and right to find the palindrome string length
## 2. Do it for both even and odd conditions
## 3. Overwrite Longest palindrome length with previous if find any
## Time - O(n*2n) -> O(n^2)
## Space - O(1)

def longestPalindromicSubstring1(string):
    currentLength = [0,1]
    for i in range(1,len(string)):
        oddlength = getLongestPalindrome(string,i-1,i+1)
        evenLength = getLongestPalindrome(string,i-1,i)
        longestLength = max(oddlength,evenLength,key = lambda x: x[1] - x[0])
        currentLength = max(currentLength,longestLength,key = lambda x: x[1]-x[0])
    return string[currentLength[0]:currentLength[1]]

def getLongestPalindrome(string,leftIdx,righIdx):
    
    while leftIdx >=0 and righIdx < len(string) :
        if string[leftIdx] != string[righIdx]:
            break
        leftIdx -= 1
        righIdx += 1
    return [leftIdx+1,righIdx]


print(longestPalindromicSubstring1("abacde"))