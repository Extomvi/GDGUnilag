i = 0
j = 0
nums1 = [1, 2, 3, 4]
nums2 = [3, 4, 5, 6, 7]
m = len(nums1)
n = len(nums2)
nums3 = []
while i < m and j < n:
    if nums1[i] < nums2[j]:
        nums3.append(nums1[i])
        i += 1
    elif nums1[i] > nums2[j]:
        nums3.append(nums2[j])
        j += 1
    elif nums1[i] == nums2[j]:
        nums3.append(nums1[i])
        i += 1
        nums3.append(nums2[j])
        j += 1

while i < m:
    nums3.append(nums1[i])
    i += 1

while j < n:
    nums3.append(nums2[j])
    j += 1

for i in range(0, len(nums1)):
    nums1[i] = nums3[i]
