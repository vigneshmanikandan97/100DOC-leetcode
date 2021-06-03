"""
Problem Statement:

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class TwoSum(object):
    def findTwoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        resultPair = []
        
        # Loop over the nums array and add each item to see if their sum is target
        i = j = 0
        while i < len(nums):
            print("i", i)
            i += 1
            j = 0
            while j < len(nums):
                print("j", j)
                j += 1
                # if nums[i] + nums[i+1] == target:
                #     resultPair.append(nums[i])
                #     resultPair.append(nums[i+1])
                # if len(resultPair) == 2:
                #     break
        
        return resultPair

ts = TwoSum()
print(ts.findTwoSum([2, 7, 11, 9], 9))
