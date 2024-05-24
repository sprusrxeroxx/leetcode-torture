# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
 

# Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

   # Best Approch is kadane algo

# This is a greedy approach to finding the maximum sum in a subarray, the algorithm first 
# increments the currSum running sum only if its sum collects gain overtime (is positive)
# if its score is greater than the maxSum so far, it sets updates the value by the current running sum
# The algorithm saves time by not considering any negative sum

import sys
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        maxSum = -sys.maxsize
        
        # Greedy Approach to Increment currSum only if it increases the value of the future sum
        for num in nums:
            currSum += num
            if currSum < num: #if currSum subarray sum is negative, reset sum starting from curr elem
                currSum = num
            if currSum > maxSum: #if currSum is greater than the current maxSum make it the maxSum
                maxSum = currSum
        return maxSum

        
