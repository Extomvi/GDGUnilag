"""Squares of a Sorted Array"""
"""Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order."""


def sortSquared(nums):
    res = []

    l, r = 0, len(nums) - 1

    while l <= r:
        if nums[l]*nums[l] > nums[r]*nums[r]:
            res.append(nums[l]*nums[l])
            l += 1
        else:
            res.append(nums[r]*nums[r])
            r -= 1

    return res[::-1]



if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(sortSquared(nums))