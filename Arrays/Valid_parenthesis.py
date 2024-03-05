##Problem Statement
'''
check a string is valid parenthesis
Example :  input = "(){}"
           output =  True
'''

## Solution -1
## Time -  O(n) | Space - O(n)
def isValid( s: str) -> bool:

    if len(s) % 2 == 1:
        return "false"
    dictP = {  '(':')', '{':'}', '[':']' }
    parList = []
    for ele in s:
        if ele in dictP:
            parList.append(ele)
        else:
            if parList and  ele == dictP[parList[-1]]:
                    parList.pop()
            else:
                return "false"

    return "true" if not parList else "false"

print(isValid("([}}])"))
        