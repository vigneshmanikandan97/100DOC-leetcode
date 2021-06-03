"""
Problem Statement:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class TwoSum(object):
    def bruteForceTwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultPair = []
        
        # Loop over the nums array and add each item to see if their sum is target
        i = 0
        while i < len(nums):
            j = 0
            while j < len(nums):
                if j != i:
                    if nums[i] + nums[j] == target:
                        resultPair.append(i)
                        resultPair.append(j)
                        return resultPair
                    else:
                        j += 1
                else:
                    j += 1
            i += 1

ts = TwoSum()
print(ts.bruteForceTwoSum([2, 5, 7, 11], 9))
