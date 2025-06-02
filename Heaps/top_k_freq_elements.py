
## Problem statement
'''
347. Top K Frequent Elements
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

'''

## solution 1
## time - O(n)  | Space - O(n)
def topKfrequent1(nums, k):

    map = {}
    res = []
    freq = [[] for i in range(len(nums)+1)]  ## creating the frq list to store the numbers based on count at the index
    
    for ele in nums:
        map[ele] = 1 + map.get(ele,0)

    for num, count in map.items():
        freq[count].append(num)

    for i in range(len(freq)-1,-1,-1):
        if freq[i]:
            res.extend(freq[i])
        if len(res) >= k:
            break

    return res


## solution 2
## Time - O(n + nlogk)   | Space - O(n+k)

import heapq
from collections import Counter
def topKFrequent2(nums,k):

    freq_map = Counter(nums)

    min_heap = []

    for num, freq in freq_map.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap,[freq,num])
        else:
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,[freq, num])
    
    return [num for freq, num in min_heap]

nums = [1,1,1,2,2,4,4,3]
k = 2

print(topKFrequent2(nums,k))  