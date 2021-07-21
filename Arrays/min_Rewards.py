### Problem Statement
'''
Write a function to reward the students fairly based on their scores by following below 2 conditions:

1. All students must receive atleast one reward
2. Any given student must receive strictly more rewards than an adjacent student
(a student immediately to left or right) with a lower score and must receive strictly fewer rewards than
an adjacent student with higher score

Example : arrayScores = [8,4,2,1,3,6,7,9,5]
          Ans = 25   // [4,3,2,1,2,3,4,5,1]

'''

### Solution - 1
## Time - O(n^2) | Space - O(n) 

def minRewards(arrScores):

    minPoints = [1] * len(arrScores)
    for i in range(1,len(arrScores)):

        if arrScores[i] > arrScores[i-1] :
            minPoints[i] = minPoints[i-1] + 1
        else:
            j = i-1
            while j>= 0 and arrScores[j] > arrScores[j+1]:
                minPoints[j] = max(minPoints[j], minPoints[j+1]+1)
                j -= 1
                
    return sum(minPoints)


### Solution - 2
## Time - O(N) | Space - O(N)

def minRewards2(arrScore):

    points = [1] * len(arrScore)

    for i in range(1,len(arrScore)):
        if arrScore[i] > arrScore[i-1]:
            points[i] = points[i-1] + 1
    
    for i in reversed(range(len(arrScore)-1)):
        if arrScore[i] > arrScore[i+1]:
            points[i] = max(points[i], points[i+1] + 1)

    return sum(points)


arrScores = [8,4,2,1,3,6,7,9,5]
print(minRewards2(arrScores))
    