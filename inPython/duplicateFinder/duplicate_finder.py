def findduplicate1(nums):
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return nums[i]

def findduplicate2(nums):
    seen = {}
    for num in nums:
        if num in seen:
            return num
        seen[num] = True

def findduplicate3(nums):
    tort = nums[0]
    hare = nums[0]
    while True:
        tort = nums[tort]
        hare = nums[nums[hare]]
        if tort == hare:
            break
    ptr1 = nums[0]
    ptr2 = tort
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    return ptr1


