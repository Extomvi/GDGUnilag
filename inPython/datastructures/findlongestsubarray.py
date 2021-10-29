"""Finding the longest Subarray by Sum"""


class Solution:
    def findLongestSubarrayBySum(self, s: int, arr: List[int]) -> int:
        result = []
        sum = 0
        left = 0
        right = 0

        while (right < arr.length):
            sum += arr[right]
            while (left < right and sum > s):
                sum -= arr[left++]

            if (sum == s and (result.length == 1 or result[1] - result[0] < right - left)):
                result = [left+1, right+1]
            
            right++

