m = len(nums2)
n = len(nums1)
ar1 = nums1
ar2 = nums2
i = 0
j = 0
m1, m2 = -1, -1
if((m + n) % 2 == 1):
    for count in range(((n + m) // 2) + 1):
        if(i != n and j != m):
            if ar1[i] > ar2[j]:
                m1 = ar2[j]
                j += 1
            else:
                m1 = ar1[i]
                i += 1
        elif(i < n):
            m1 = ar1[i]
            i += 1

    # for case when j<m,
        else:
            m1 = ar2[j]
            j += 1
    print(m1)

    # median will be average of elements
    # at index ((m + n)/2 - 1) and (m + n)/2
    # in the array obtained after merging ar1 and arr2
else:
    for count in range(((n + m) // 2) + 1):
        m2 = m1
        if(i != n and j != m):
            if ar1[i] > ar2[j]:
                m1 = ar2[j]
                j += 1
            else:
                m1 = ar1[i]
                i += 1
        elif(i < n):
            m1 = ar1[i]
            i += 1

            # for case when j<m,
        else:
            m1 = ar2[j]
            j += 1
print((m1 + m2)/2)
