### Two Number Sum
def twoNumberSum(array, targetSum): #O(n^2) Operation
    # Write your code here.
	for items in range(len(array)):
		first_item = array[items]
		for num in range(items+1, len(array)):
			second_item = array[num]
			if first_item + second_item == targetSum:
				return [first_item, second_item]
	return []

def twoNumberSum(array, targetSum): # O(n) Solution
    # Write your code here.
	nums = {}
	for num in array:
		target = targetSum - num
		if target in nums:
			return [target, num]
		else:
			nums[num] = True
	return []

def twoNumberSum(array, targetSum): # O(nlogn) Solution
    # Write your code here.
	array.sort()
	left = 0
	right = len(array) -1
	while left < right:
		result = array[left] + array[right]
		if result == targetSum:
			return [array[left], array[right]]
		elif result < targetSum:
			left += 1
		elif result > targetSum:
			right -= 1
	return []

print(twoNumberSum([2,4,5,-2,43,79,1,45,2,56,7,3,2,45,6,2,1,10,6,9], 15))

    
