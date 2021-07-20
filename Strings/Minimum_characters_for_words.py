### Problem Statement
'''
Write a function that takes array of words and returns the smallest array of characters needed to
form all the words.

Example :  words = ["your","you","or","yo"]
           ans = ["y","o","r","u"]

'''

### Solution - 1
## Time - O(N*l)  | Space - O(c)
## n - number of words, l - length of longest word
## c - number of unique characters across words

def minCharactersForWords(arrWords):

    minChars = {}
    
    for word in arrWords:
        wordChars = {}
        for letter in word:
            wordChars[letter] = wordChars.get(letter,0) + 1
        
        for key, value in wordChars.items():
            minChars[key] = max(minChars.get(key,value), value)
        
    minCharslist =[]
    for key , value in minChars.items():
        minCharslist.extend([key]*value)
    
    return minCharslist


print(minCharactersForWords(["your","rr"]))
  