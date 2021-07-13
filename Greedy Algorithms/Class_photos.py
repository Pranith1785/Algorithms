### Problem Statement
'''
Even number of students in class and exactly half are wearing red shirt and other half blue.
photograpgher need to arrange the students in two rows having same number of students and should follow below rules:

1. All students wearing red shirts must be in same row
2. All Students wearing blue shirts must be in same row
3. Each student in back row must be strictly taller than the student directly in front of them in front row

Write a function , whether photograph is possible or Not

Example : redShirtHeights: [5, 8, 1, 3, 4],
          blueShirtHeights: [6, 9, 2, 4, 5]

    Ans :  True (blue shirts student will be in back row)

'''


### Solution - 1
## Time - o(nlogn)  | Space - O(1) 

def classPhotos(redShirtsHeights,blueShirtsHeights):

    redShirtsHeights.sort()
    blueShirtsHeights.sort()

    backRow = "redShirts" if max(redShirtsHeights) > max(blueShirtsHeights) else "blueShirts"

    for idx in range(len(redShirtsHeights)):
        redShirt = redShirtsHeights[idx]
        blueShirt = blueShirtsHeights[idx]

        if backRow == "blueShirts" :
            if redShirt >= blueShirt:
                return False
        else:
            if blueShirt >= redShirt:
                return False
    return True


redShirtHeights = [5, 8, 1, 3, 4]
blueShirtHeights =  [6, 9, 2, 4, 5]
print(classPhotos(redShirtHeights,blueShirtHeights))
