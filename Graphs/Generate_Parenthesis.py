### Probelm Statement
''' Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''

### Example 1:
'''
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
''' 

## solution 1
## Time - o(n!) | Space - O(n!)

from itertools import permutations

def isValid_parenthesis(string : str) -> bool:
    bracket_dict = {'(':')'}

    if len(string) % 2 == 1:
        return False
    parList = []
    for ele in string:
        if ele in bracket_dict:
            parList.append(ele)
        else:
            if parList and ele == bracket_dict[parList[-1]]:
                parList.pop()
            else:
                return False
    return True if not parList else False

def generate_Parenthesis(n: int) -> list[str]:
    brackets = ['(',')']
    brackets = brackets * n
    getAll_Parenthesis = list(set([ "".join(eachList) for eachList in permutations(brackets,n*2) if (eachList[0] != ")" and eachList[-1] != "(")]))
    getValid = [ eachParenthesis for eachParenthesis in getAll_Parenthesis if isValid_parenthesis(eachParenthesis)]
    return getValid

print(generate_Parenthesis(3))

### Solution - 2
## time complexity -   | Space complexity - 

def generate_Parenthesis1(n: int) -> list[str]:

    def dfs(left,right,string):

        if len(string) == n*2:
            res.append(string)
        
        if left < n:
            dfs(left+1, right, string + "(")
        
        if right < left:
            dfs(left, right+1,string + ")")

    res = []

    dfs(0,0,'')

    return res

print(generate_Parenthesis1(3))
