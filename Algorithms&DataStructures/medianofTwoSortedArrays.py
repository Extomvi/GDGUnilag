"""Median of Two Sorted Arrays"""

def medianSortedArrays(nums1, nums2):
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2
    print(total, half)

    if len(B) < len(A):
        B, A = A, B
        #print(A, B)
    
    l, r = 0, len(A)-1
    #print(l, r)
    while True:
        i = (l + r) // 2
        j = half - i - 2

        Aleft = A[i] if i >= 0 else float("-infinity")
        Aright = A[i + 1] if (i+1) < len(A) else float("infinity")
        Bleft = B[j] if j >= 0 else float("-infinity")
        Bright = B[j + 1] if (j+1) < len(B) else float("infinity")
        
        if Aleft <= Bright and Bleft <= Aright:
            if total % 2:
                return min(Aright,Bright)
            return (max(Aleft,Bleft) + min(Aright, Bright)) / 2
        elif Aleft > Bright:
            r = i - 1
        else:
            l = i + 1





if __name__ == "__main__":
    nums1 = [1,2]
    nums2 = [3,4]
    print(medianSortedArrays(nums1,nums2))