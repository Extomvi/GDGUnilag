"""Binary searching algorithm"""
class Solution:
    def binarysearch(a, x):
        # a = [1,4,3,3,4,7,8,28,42,71]
        l = 0
        r = len(a) - 1

        while l <= r:
            mid = (l + r) // 2
            if a[mid] > x:
                r = mid - 1
            elif a[mid] < x:
                l = mid + 1
            else:
                return mid

        return -1
    print(binarysearch([1,3,3,4,7,8,28,42,71], 7))
