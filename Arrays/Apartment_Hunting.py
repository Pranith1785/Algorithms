## Problem Statement
'''
Function that returns the location of block that is most optimal for user based on his/her requirements

Ex : buildingBlocks = [ {"gym": False,"school": True,"store": False},
                    {"gym": True,"school": False,"store": False},
                    {"gym": True,"school": True,"store": False},
                    {"gym": False,"school": True,"store": False},
                    {"gym": False,"school": True,"store": True} ]

    reqs = ["gym", "school", "store"]

    bestblock = 3 (with in 1 block distance all the gym,school and stores are available)
'''


## Solution - 1
## Time - O(n^2 * r) | space - O(n)

def calBlockDistance(currentBlock, otherBlock, reqs):
    return [eachReq for eachReq in reqs if otherBlock[eachReq] is True]


def apartmentHunting(blocks, reqs):

    listDistance = []

    for idx in range(len(blocks)):
        left = idx-1
        right = idx +1

        distance = 0
        needReq = [eachReq for eachReq in reqs if not blocks[idx][eachReq]]

        while(len(needReq) >0 and(left >= 0 or right <= len(blocks)-1) ):
            leftMatchReq = []
            rightMatchReq =[]
            leftDistance = 0
            rightDistance = 0
            
            if left >= 0 :
                leftMatchReq = calBlockDistance(blocks[idx],blocks[left],needReq)
                if(len(leftMatchReq) > 0 ):
                    leftDistance = idx-left
                    needReq = [eachReq for eachReq in needReq if eachReq not in leftMatchReq ]
                left -= 1
            
            if right <= len(blocks)-1:
                rightMatchReq = calBlockDistance(blocks[idx],blocks[right],needReq)
                if(len(rightMatchReq)>0):
                    rightDistance = right - idx
                    needReq = [eachReq for eachReq in needReq if eachReq not in rightMatchReq ]
                right += 1       

            distance = max(distance,leftDistance,rightDistance)
        
        listDistance.append(distance)
    
    return (listDistance.index(min(listDistance)))


buildingBlocks = [ {"gym": False,"school": True,"store": False},
                    {"gym": True,"school": False,"store": False},
                    {"gym": True,"school": True,"store": False},
                    {"gym": False,"school": True,"store": False},
                    {"gym": False,"school": True,"store": True} ]

reqs = ["gym", "school", "store"]
print(apartmentHunting(buildingBlocks,reqs))


