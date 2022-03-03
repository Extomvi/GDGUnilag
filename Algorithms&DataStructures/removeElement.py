"""Remove Element"""
"""Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The relative order of the elements may be changed."""

def removeElement(nums, val):
    k = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[i] = nums[k]
            k += 1
    return k



if __name__ == "__main__":
    nums = [3,2,2,3]
    val = 3
    print(removeElement(nums, val))
