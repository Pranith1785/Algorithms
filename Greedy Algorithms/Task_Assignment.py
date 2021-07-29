### Problem Statement
'''
Given a integer k representing number of workers and array of positive integers representing 
duration of tasks that must be completed by workers. Number of tasks equal to 2k and each worker need to
complete exactly 2.
Workers will complete the tasks in parallel and time taken complete all tasks will be equal to time taken to
complete the longest pairs of tasks.

Write function that returns the indices of the tasks completed each worker in pair.

Example : k = 3
          tasks = [1,3,5,3,1,4]

        Ans = [ 
                [0,2], //tasks[0] = 1, tasks[2] = 5 | 1 + 5 = 6
                [4,5], //tasks[4] = 1, tasks[5] = 4 | 1 + 4 = 5
                [1,3]  //tasks[1] = 3, tasks[3] = 3 | 3 + 3 = 6
              ]

'''

### Solution - 1
## Time - O(nlogn)  | Space - o(n) //where n is 2times of k

def taskAssignment(k,tasks):

    pairedTasks = []
    taskDurationToIndices = getTasksDurationToIndices(tasks)

    print(taskDurationToIndices)
    sortedTasks = sorted(tasks)

    for idx in range(k):
        task1Duration = sortedTasks[idx]
        indicesTask1Duration = taskDurationToIndices[task1Duration]
        task1Index = indicesTask1Duration.pop()

        task2Duration = sortedTasks[(2*k)-1-idx]
        indicesTask2Duration = taskDurationToIndices[task2Duration]
        task2Index = indicesTask2Duration.pop()

        pairedTasks.append([task1Index,task2Index])

    return pairedTasks

def getTasksDurationToIndices(tasks):

    tasksDurationToIndices = {}
    for idx, value in enumerate(tasks):
        if value not in tasksDurationToIndices:
            tasksDurationToIndices[value] = [idx]
        else:
            tasksDurationToIndices[value].append(idx)
    return tasksDurationToIndices

k = 3
tasks = [1,3,5,3,1,4]

print(taskAssignment(k,tasks))
