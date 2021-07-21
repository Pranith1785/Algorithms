### Problem Statement
'''
Find the maximum or minimum possible of total speed of tandem bicycles being ridden
Provided with two list of positive integers : contains speeds of rider wearing red and blue shirts.
Each bicycle has a one blue and redshirt riders.And rider with max speed will be the bicycle speed

For example : redShirtRider = 5 , blueShirtRider = 3, bicycle speed = 5

Now if input parameter fastest = True, find max total speed
                                else  min total speed

Example : redShirtsSpeeds = [5,5,3,9,2]
          blueShirtsSpeeds = [3,6,7,2,1]
          fastest = True

          Answer = 32 // [[5,3],[5,2],[9,1],[2,7],[3,6]]
'''

### Solution - 1
## Time - O(NlogN)  | Space - O(1)

def tandemBicycleSpeed(redShirtSpeeds, blueShirtSpeeds, fastest):

    redShirtSpeeds.sort()
    blueShirtSpeeds.sort()

    totalSpeed = 0
    ridersCount = len(redShirtSpeeds)

    for i in range(ridersCount):
        if fastest :
            totalSpeed += max(redShirtSpeeds[i], blueShirtSpeeds[ridersCount-1- i])
        else:
            totalSpeed += max(redShirtSpeeds[i],blueShirtSpeeds[i])

    return totalSpeed


redShirtSpeeds = [5,5,3,9,2]
blueShirtSpeeds = [3,6,7,2,1]
fastest = False

print(tandemBicycleSpeed(redShirtSpeeds,blueShirtSpeeds,fastest))
