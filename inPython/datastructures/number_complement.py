"""Number Complement"""

'''
Given a positive integer, output it's complement number.
The complement strategy is to flip the bits of its binary representation.
'''
import math
class Solution:
    """Using the math/log built in function"""
    def findComplement(self, num: int) -> int:
        return 2**(int(math.log2(num) + 1)) - num - 1

    def findComplement2(self, nums: int) -> int:    #Using our own function and other operations.
        def to_binary(nums):
            return bin(nums)[2:]
        def to_decimal(nums):
            return int(nums,2)

        def helper(nums):
            rev = to_binary(nums)
            comp = ['1' if x == '0' else '0' for x in rev]
            comp.insert(0, '0b')
            return to_decimal(''.join(comp))
        num = helper(nums)
        return num
