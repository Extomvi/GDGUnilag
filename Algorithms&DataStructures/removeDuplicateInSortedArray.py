"""Remove Duplicates in Sorted Arrray"""

def removeDuplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1
    return l



if __name__ == "__main__":
    nums = [1,1,2]
    print(removeDuplicates(nums))