""" Shuffling the array program """

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shift = n
        i = 0
        while i < 2 * (n-1):
            currNum = nums[shift]
            j = shift
            while j > i + 1:
                nums[j] = nums[j - 1]
                j -= 1
            nums[i+1] = currNum
            print(nums)
            shift += 1
            i += 2
        return nums
