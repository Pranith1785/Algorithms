
'''
Create a function which returns whether a document can be created using the available character

Ex : string = "abcabc" , document = "aabbccc"
     output = FALSE (one 'c' is missing in string)
'''

### Solution 1
## Time - O(n*m)   | Space - O(1)

def generateDocument(characters,document):

    for ele in characters:
        document =  document.replace(ele,"",1)
    return True if len(document) == 0 else False


### Solution 2
## Time - O(n+m)  | Space - O(c)

def generateDocument2(characters,document):

    characterCounts = {}

    for ele in characters:
        if ele not in characterCounts:
            characterCounts[ele] = 0
        
        characterCounts[ele] += 1

    for ele in document:
        if ele not in characterCounts or characterCounts[ele] == 0:
            return False
        characterCounts[ele] -= 1

    return True


characters = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(generateDocument2(characters,document))