### Problem Statement
''''
Function that takes the execution time of a queries in array format 
and gives the minimum waiting time taken to execute all the queries. 

Order of queries can be modified
Example : queries = [4,1,5]
        Ans = 6  for [1,4,5]
'''

### Solution -1
## Time - O(Nlog(N)) | Space - O(1)
def minimumWaitingTime(queries):

    queries.sort()
    waitingTime = 0
    for i in range(1, len(queries)):
        waitingTime += sum(queries[:i])
    
    return waitingTime


print(minimumWaitingTime([4,1,5]))