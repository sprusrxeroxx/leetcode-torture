#PROBLEM STATEMENT
# 11. Container With Most Water
# Medium
# Topics
# Companies
# Hint
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1



# The GREEDY Solution I came up with

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # heightLine is a straightline that will descend from the heighest point/s until it meets the x-axis
        # Think of it as a horizontal line/window that senses the bars it touches
        heightLine = max(height)
        maxArea = 1
        i = 0
        # At the current height I check which bars exist 
        while heightLine > 0:
            elems = [h for h in height if h >= heightLine]

            leftmost = height.index(min(elems))  # Index of the leftmost bar in elems
            rightmost = height.index(max(elems))  # Index of the rightmost bar in elems

            # Then I subtract the one's furthest apart in the elems list, finding the max distance for the given set
            x = abs(rightmost - leftmost)

            # Here i find the max absolute value of the volume for the current height
            Area = abs(x * heightLine)

            #if the current area is greater than maxArea, then i make it the maxArea
            if Area > maxArea:
                maxArea =  Area
            
            print("Area:{}  maxArea:{}  elems:{}  heightLine:{}  x:{}".format(Area, maxArea, elems, heightLine, x))
            # print("min:{} max:{}".format(height.index(min(elems)), height.index(max(elems)) ))
            heightLine -=1
        return maxArea


# Final Inefficient version, ended up using the ubiquitous two pointer method for the final submission, overall I'm way more proud of this than the efficient algothrithm
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         # heightLine is a straightline that will descend from the heighest point/s until it meets the x-axis
#         # Think of it as a horizontal line/window that senses the bars it touches
#         heightLine = max(height)
#         maxArea = 0
#         i = 0
#         # At the current height I check which bars exist 
#         while heightLine > 0:
#             elems = [h for h in height if h >= heightLine]
            
#             if len(elems) == 1:
#                 x = 0
#                 Area = abs(x * heightLine)
#             elif not elems:
#                 x = 0
#                 Area = abs(x * heightLine)
#             else:
#                 leftmost = float('inf')
#                 rightmost = -1

#                 for i, val in enumerate(height):
#                     if val >= heightLine and i < leftmost:
#                         leftmost = i
#                     if val >= heightLine and i > rightmost:
#                         rightmost = i

#                 x = abs(rightmost - leftmost) if leftmost != float('inf') and rightmost != -1 else 0


#                 # Here i find the max absolute value of the volume for the current height
#                 Area = abs(x * heightLine)

#                 #if the current area is greater than maxArea, then i make it the maxArea
#             maxArea = max(maxArea,Area)
                
#                 #print("Area:{}  maxArea:{}  elems:{}  heightLine:{}  x:{}".format(Area, maxArea, elems, heightLine, x))
#                 # print("min:{} max:{}".format(height.index(min(elems)), height.index(max(elems)) ))
#             heightLine -=1
#         return maxArea






 
