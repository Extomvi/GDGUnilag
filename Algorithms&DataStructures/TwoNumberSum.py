o(n^2) Solution
def twoNumSum(array, target):
    for i in range(len(array) - 1):
        first = a[i]
        for j in range(i+1, len(array)):
            second = a[j]
            if second + first == target:
                print([first, second])
    return []
    
print(twoNumSum([2,4,5,-2,43,79,1,45,2,56,7,3,2,45,6,2,1,10,6,9], 15))     
        
    
