### Problem
'''
Find the nth Fibonacci number.
    Fib1 = 0
    Fib2 = 1
    Fib3 = Fib1 + Fib2
'''

### Solution 1
# Time Complexity - O(n)
# Space Complexity - O(1)
def getNthFib(n):
    fib1 = 0
    fib2 = 1
    if n > 2:
        for _ in range(2,n):   # Use While 
            fib3 = fib1 + fib2
            fib1 = fib2
            fib2 = fib3
        return fib3
    return 1 if n>1 else 0

### Solution 2
'''
using Recursion
'''
# Time Complexity - O(2^n)
# Space Complexity - O(n)
def getNthFib2(n):
    if n == 1:
        return 0
    elif n == 2 :
        return 1
    else:
        return getNthFib(n-1) + getNthFib(n-2)

### Solution 3
'''
using Recursion
'''
# Time Complexity - O(n)
# Space Complexity - O(n)
def getNthFib3(n,memoize = {1:0,2:1}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = getNthFib3(n-1,memoize) + getNthFib3(n-2,memoize)
        return memoize[n]


print(getNthFib3(10))