"""
Problem statement:

Given an array nums of integers, return how many of them contain an even number of digits.
"""
class EvenDigits(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        
        return count