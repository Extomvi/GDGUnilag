def findNumber(array, targetNum):
    # Write your code here.
    array.sort()
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = (left+right) // 2
        if array[mid] == targetNum:
            return mid
        elif array[mid] > targetNum:
            right = mid - 1
        else:
            left = mid + 1
    return -1
             
print(findNumber([2,4,5,-2,43,79,1,45,2,56,7,3,2,45,6,2,1,10,6,9], 5))
