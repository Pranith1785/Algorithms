### Problem Statement
'''
Function that takes the string of words separated by one or more spaces and 
returns the string with words in reverse order.

Example : string =  "Space b/w words   is 4"
          Ans    =  "4 is   words b/w Space"

'''

### Solution - 1
## Time - O(n) | Space - O(n) n- length of the string

def reverseWordsInString(string):
    words = string.split(" ")
    return " ".join(words[::-1])


### Solution -2
## Time - O(n) | Space -  O(n) 

def reverseWordsInString2(string):
    wordList = []
    startIdx = 0 
    for i in range(0,len(string)):
        currentChar = string[i]

        if currentChar == " ":
            wordList.append(string[startIdx:i])
            startIdx = i
        elif string[startIdx] == " ":
            wordList.append(" ")
            startIdx = i
    
    wordList.append(string[startIdx:])
    reverseList(wordList)

    return "".join(wordList)

def reverseList(arrlist):
    start, end = 0, len(arrlist)-1
    while start < end:
        arrlist[start], arrlist[end] = arrlist[end],arrlist[start]
        start += 1
        end -= 1




print(reverseWordsInString2("saf afsjfa   kfah"))
