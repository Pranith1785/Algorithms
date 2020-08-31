

### Solution 1
# Time Complexity - O(n^2)
# Space Complexity - O(1) 
def twoNumberSum1(array, targetSum):
    # Write your code here.
	for i in range(0,len(array)-1):
		firstNum = array[i]
		for j in range(i+1,len(array)):
			secondNum = array[j]
			if firstNum + secondNum == targetSum :
				return [firstNum,secondNum]
	return []


### Solution 2
# Time Complexity - O(n)
# Space Complexity - O(n)

def twoNumberSum2(array,targetSum):
    num_dict = {}
    for num in array:
        remValue = targetSum - num
        if remValue in num_dict:
            return [remValue,num]
        else:
            num_dict[remValue] = True
    return []


### Solution 3
# Time Complexity - O(n)
# Space Complexity - O(n)

def twoNumberSum3(array,targetSum):

    array.sort()
    left = 0
    right = len(array)-1

    while left < right :
        currentSum = array[left] + array[right]
        if currentSum == targetSum :
            return [array[left],array[right]]
        elif currentSum > targetSum :
            right -= 1
        else:
            left += 1
    
    return []




arr = [3, 5, -4, 8, 11, 1, -1, 6]
target = 10


print(twoNumberSum3(arr,target))