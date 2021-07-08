### Problem Statement
'''
Write a function that takes an non-empty array of integers and 
returns the array of same length where ech element is product of every other element in the array

Example :  array = [5, 1, 4, 2]
           Ans = [8, 40, 10, 20]
           [8 = 1* 4*2 , 40 = 5*4*2, 10 = 5*1*2, 20 = 5*1*4]

'''

### Solution - 1
## Time - O(N^2)  | Space - O(N)

def arrayOfProducts(array):

    arrProduct = []

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                runningProduct *= array[j]
        arrProduct.append(runningProduct)

    return arrProduct


## Solution 2
## Time - O(N) | Space - O(N)

def arrayOfProducts2(array):
    arrProduct = [1 for _ in range(len(array))]
    leftProduct = [1 for _ in range(len(array))]
    rightProduct = [1 for _ in range(len(array))]

    leftRunningProduct  =1
    for i in range(len(array)):
        leftProduct[i] = leftRunningProduct
        leftRunningProduct *= array[i]

    rightRunningProduct = 1
    for i in range(len(array)-1,-1,-1):
        rightProduct[i] = rightRunningProduct
        rightRunningProduct *= array[i]

    for i in range(len(array)):
        arrProduct[i] = leftProduct[i] * rightProduct[i]

    return arrProduct
        
print(arrayOfProducts2([5,1,4,6]))

