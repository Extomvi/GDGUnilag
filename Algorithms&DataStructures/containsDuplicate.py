"""Contains Duplicate"""

def containsDuplicate(nums):
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)


if __name__ == "__main__":
    nums = [1,2,3,1]
    print(containsDuplicate(nums))