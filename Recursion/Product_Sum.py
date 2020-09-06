### Problem Statement
'''
The product sum of the special array is the sum of its element, 
where special array inside it are summed themselves and then multiplied by their level depth
Ex : array = [x, y, [a,b] ,c, [[d,e],f]]
     solution = x + y + 2*(a+b) + c + 2*(3*(d+e)+f)
'''

## Solution 1
## TIme - O(n) | length of array including the sub elements
## Space - O(d) | depth of the nested array 
def productSum(array,i=1):
    totalValue = 0
    for ele in array:
        if isinstance(ele,list):  ## type(ele) is list
            totalValue +=  (i+1) * productSum(ele,i+1)
        else:
            totalValue += ele
    return totalValue

array = [1,[[2]]] 

print(productSum(array,1))