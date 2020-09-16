### Problem Statement
'''
Write a function that takes array of words and groups anagram together
Anagram - words which has same alphabets but not in order
        ex : "act" and "act"
'''

### Solution 1
## Time - O(n*n*m) ; n - no of words ; m - length of longest word
## Space - O(n*m + n)

def groupAnagrams(arrWords):
    arrAnagrams = []
    checkIndex = [False] * len(arrWords)
    for i in range(0,len(arrWords)):
        if not checkIndex[i]:
            newAnagram = [arrWords[i]]
            for j in range(i+1,len(arrWords)):
                if len(arrWords[i]) == len(arrWords[j]) and checkAnagram(arrWords[i],arrWords[j]):
                    newAnagram.append(arrWords[j])
                    checkIndex[j] = True
            arrAnagrams.append(newAnagram)
    return arrAnagrams

def checkAnagram(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    for letter in list1:
        try:
            list2.remove(letter)
        except:
            return False
    return True


### Solution 2
## Time - O(n*m*log(m))
## Space - O(n*m)

def groupAnagrams1(arrWords):
    if len(arrWords) == 0:
        return []
    dictAnagrams = {}

    for word in arrWords:
        newWord = "".join(sorted(word))
        if newWord in dictAnagrams:
            dictAnagrams[newWord].append(word)
        else:
            dictAnagrams[newWord] = [word]
    
    return list(dictAnagrams.values())

arrWords = ["yo", "act", "flop", "tac", "foo", "cat", "oy", "olfp"]
print(groupAnagrams1(arrWords))