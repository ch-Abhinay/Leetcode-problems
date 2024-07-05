# # 53. Maximum Subarray
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
# Code:
class Solution(object):
    def maxSubArray(self, nums):
        cmax=0
        maxval=-99999999999
        for num in nums:
            cmax= max(cmax+num,num)
            maxval=max(maxval,cmax)
        return maxval
