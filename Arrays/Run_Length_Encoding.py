## Problem statement
'''
Convert the given lengthy string to encoding string
Ex :  string = "AAAABBCCCCCD"
      Ans = ""4A2B5CD"
'''

## Solution 1
## Time - O(nm) n- length of string, m - 
## Space - O(n)

def encodeString(encodeStr, letter, count):
    
    if count > 9 :
        iLoop = count//9
        rem = count%9
        for _ in range(iLoop):
            encodeStr += "9" + letter
        if rem > 0:
            encodeStr +=  str(rem) + letter
    else:
        encodeStr += str(count) + letter

    return encodeStr

def runLengthEncoding(string):

    currentLetter = string[0]
    count = 0
    finalString = ""
    for i in range(len(string)):
        alphabet  = string[i]

        if alphabet == currentLetter:
            count += 1
        else:
            finalString = encodeString(finalString, currentLetter, count)
            currentLetter = alphabet
            count = 1

    finalString = encodeString(finalString, alphabet, count)   
    return finalString

## Solution 2
## Time - O(n)
## Space - O(n)
def runLengthEncoding2(string):

    finalString = ""
    count = 1
    for idx in range(1,len(string)):
        prevLetter = string[idx-1]
        currentLetter = string[idx]
        if prevLetter !=  currentLetter or count == 9:
            finalString += str(count) + prevLetter
            count = 0
        count += 1
    finalString += str(count) + string[len(string)-1]
    return finalString

print(runLengthEncoding2("AAAAAAAAAAAAABBCCCCDD"))
        