def bubble_sort(nums):
    swap = False
    for i in range(len(nums), 0, -1):
        for j in range(i-1):
            if nums[j] > nums[j+1]:
                swap = True
                nums[j], nums[j+1] = nums[j+1], nums[j]
            if not swap:
                return nums
        return nums