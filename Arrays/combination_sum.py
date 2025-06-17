## Problem statement
'''
39. Combination Sum
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times.
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]

'''

## Solution 1
# Time: O(2^target)  | Space: O(n)

def combinationSum(candidates, target):
    res = []

    def dfs(i,curr, total):

        if total == target:
            res.append(curr.copy())
            return

        if  i >= len(candidates) or total > target:
            return
        
        curr.append(candidates[i])
        dfs(i,curr, sum(curr))
        curr.pop()
        dfs(i+1,curr, sum(curr))

    dfs(0,[],0)
    return res


## Solution 2
def combinationSum2(candidates, target):

    def backtrack(start, target, comb):
        if target == 0:
            result.append(comb)
            return
        
        if target < 0:
            return
        
        for i in range(start,len(candidates)):
            backtrack(i, target-candidates[i], comb + [candidates[i]])

    result = []
    candidates.sort()
    backtrack(0,target,[])
    return result


candidates = [2,3,6,7]
target = 7
print(combinationSum2(candidates, target))



