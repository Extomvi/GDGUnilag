"""Longest Consecutive Element 2"""


def longest_consecutive_elements(nums):
    seen = set(nums)
    res = []
    for num in nums:
        if num-1 not in seen:
            start = num
            while num in seen:
                num += 1
                res.append('{}->{}'.format(start, num))
    return res
