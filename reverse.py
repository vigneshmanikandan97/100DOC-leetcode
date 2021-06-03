"""
Problem statement:

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned)
"""

class ReverseA32BitInteger(object):
    def reverseInteger(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = [1, -1][x < 0]
        rn = sign * int(str(abs(x))[::-1])

        return rn if -(2**31 - 1) < rn < (2**31 - 1) else 0

ra32int = ReverseA32BitInteger()
print(ra32int.reverseInteger(-9988))