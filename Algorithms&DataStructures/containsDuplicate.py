"""Contains Duplicate"""

def containsDuplicate(nums):
    hashset = set()

    for n in range(len(nums)):
        if nums[n] in hashset:
            return True
        hashset.add(nums[n])


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))