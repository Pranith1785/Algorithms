
## Problem Statement
'''
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

'''

## Solution 1
## time - O(n) | Space - O(1)

def climbStairs(n: int) -> int:

    step1 = 1
    step2 = 2
    if n == 1:
        return step1
    if n==2 :
        return step2

    i = 2
    while(i<n):
        total_step = step1 + step2
        i += 1
        step1,step2 = step2, total_step

    return total_step

