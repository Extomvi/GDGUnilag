"""Finding the Majority Element in a List"""

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                count +=1
                if count > len(nums)/2:
                    return nums[i]
                else:
                    count = 1
            return nums[0]