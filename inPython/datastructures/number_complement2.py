"""Number compliment Solution using swaping of binary and decimal integers"""
class Solution:
    def findComplement2(self, nums: int) -> int:
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