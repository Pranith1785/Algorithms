### Problem statement
'''
Create a function which take non-empty lower string and key, output the new string after shifting every letter in the string by a non-negative integer(key)
Ex : string = "xyz" , key = 2
     output = "zab"
'''

### Solution 1
# Time - O(n^2)
# Space - O(n)
def caesarCipherEncryptor(string,key):
    key = key%26
    newString = ""
    for i in string:
        num = ord(i) + key
        if num > 122:
            num = num - 122 - 1 + 97
        newString += chr(num)
    return newString

### Solution 2
# Time - O(n)
# Space - O(n)
def caesarCipherEncryptor2(string,key):
    key = key%26
    newString = []
    for i in string:
        num = ord(i) + key
        if num > 122:
            num = num - 122 - 1 + 97
        newString.append(chr(num))
    return "".join(newString)


### Solution 3
# Time - O(n)
# Space - O(n)
def caesarCipherEncryptor3(string,key):
    key = key%26
    alphabets = list("abcdefghijklmnopqrstuvwxyz")
    newString = []
    for i in string:
        newString.append(alphabets[(alphabets.index(i) + key)%26])
    
    return "".join(newString)

print(caesarCipherEncryptor3("xyzab",27))


