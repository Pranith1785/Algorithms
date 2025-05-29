## Problem statement
'''
A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1:

Input: n = 19
Output: true
Explanation:
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1

'''

## Solution - 1
## time - o(n)  | Space - O(n)

def squareNumber(n):
    ss = 0
    while n>0:
        digit = n % 10
        ss += digit ** 2
        n = n//10
    return ss


def happyNumber(num:int) -> bool:

    ss_num = set()
    
    while num not in ss_num:
        ss_num.add(num)
        num = squareNumber(num)

        if num == 1:
            return True

    return False


## Solution 2
## time - o(n)  | space - O(1)
def happyNumber2(num):
    slow,fast = num, squareNumber(num)

    while slow != fast and fast != 1:
        slow = squareNumber(slow)
        fast = squareNumber(squareNumber(fast))

        if slow == fast:
            return False
        
    return True


print(happyNumber2(19))