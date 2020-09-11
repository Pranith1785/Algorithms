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


print(longestPalindromicSubstring("abcdefggfedcba"))