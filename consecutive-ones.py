"""
Problem statement:

Given a binary array nums, return the maximum number of consecutive 1's in the array.
"""

class ConsecutiveOnes(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currSum = mainSum = 0
        for num in nums: # [1,1,0,1,1,1]
            if num == 1:
                currSum += num
            else:
                currSum = 0
            
            # Copy current sum to main sum
            if currSum > mainSum:
                mainSum = currSum
                
        return mainSum
