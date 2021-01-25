a = [2,3,4,5,6,7]
target = 7
for i in range(len(a)):
    first = a[i]
    for j in range(i+1, len(a)):
        second = a[j]
        if second + first == target:
            print([first, second])
    
        
        
    
