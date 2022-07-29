"""Finding duplicate numbers in an array"""

def duplicates(nums):
    
    for num in nums:
        if nums[abs(num)] >= 0:
            nums[abs(num)] = -nums[abs(num)]
        else:
            return abs(num)


if __name__ == "__main__":
    nums = [2,3,4,1,3,6, 2]
    duplicates(nums)
