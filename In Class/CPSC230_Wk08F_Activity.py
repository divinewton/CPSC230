# Class Activities

### If you weren't able to finish this on Wednesday, work on it today
### NOTE: Add a docstring to your distance function
'''
0.  Distance Formula
    NOTE: Add default arguments for pt1 (pt1 = [0,0])
    Write a functions that calculates the distance between two points
    https://en.wikipedia.org/wiki/Distance (just 2D distance is fine)
        - The function should take 2 lists as inputs
            - pt1 = [x1, y1]
            - pt2 = [x2, y2]
        - The function should return the distance
        - Remember that a distance cannot be a negative number
        - BONUS 01: Write your script so that the user can enter the 
          X and Y coordinates of their two points
        - BONUS 02: Write your function so it only returns 3 
          significant digits
    
    NOTE: Add to your function to give the user the option to cauclulate 
          either Euclidean or Manhattan distance (Euclidean) is the formula 
          you used Monday, Manhattan is linked here:
          https://algodaily.com/lessons/what-is-the-manhattan-distance
'''
## The answer with these coordinates will be 13.928 (Euclidean)
# pt1 = [5, 2]
# pt2 = [10, 15]

pt1x = int(input("Enter x coordinate of first point: "))
pt1y = int(input("Enter y coordinate of first point: "))
pt1 = [pt1x, pt1y]
pt2x = int(input("Enter x coordinate of second point: "))
pt2y = int(input("Enter y coordinate of second point: "))
pt2 = [pt2x, pt2y]

def distance(pt1 = [0,0],pt2 = [0,0]):
    import math
    d1 = math.sqrt(((pt2[0] - pt1[0]) ** 2) + ((pt2[1] - pt1[1]) ** 2))
    if d1 >= 0:
      return d1
    else:
      d1 == 0
      return d1
    
print("The distance between the two points is", round(distance(pt1,pt2),3))

'''
1.  Team up with 1-2 folks at your table. Share your progress with the 
    project (you can use your table monitors if that's easier). 
    
    If all of you are finished with your code, share and play each 
    others games and give feedback. Consider:
        1) How could your classmates make their game more interactive?
        2) How could they make it more user-friendly?
        3) Are there enough comments in their code?
    
    If some of you are still working, help your classmates brainstorm 
    and debug their code.

    Nothing to turn in for this one.
'''
