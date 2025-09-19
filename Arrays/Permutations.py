### Problem Statement
'''
46. Permutations

Given an array `nums` of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:
Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:
Input: nums = [1]
Output: [[1]]

Constraints:
*   `1 <= nums.length <= 6`
*   `-10 <= nums[i] <= 10`
*   All the integers of `nums` are unique.
'''

### Solution
### Time - O(n * n!) | Space - O(n * n!) auxiliary space - O(n)
def permutations(nums: list[int]) -> list[list[int]] :

    path = []
    result = []
    used = {num : False for num in nums}
    
    def backtrack():

        if len(nums) == len(path):
            result.append(path[:])
            return
        
        for num in nums:
            if not used[num]:
                used[num] = True
                path.append(num)

                backtrack()

                path.pop()
                used[num] = False

    backtrack()

    return result


print(permutations([1,2]))
        

            

