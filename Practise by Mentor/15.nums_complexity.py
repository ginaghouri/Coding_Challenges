nums1 = [1, 2, 3, 4]
nums2 = [5, 6, 7, 8, 9, 10]

# M - length of nums2
# O(N + M)
def example(nums1, nums2):
    for i in nums1:
        print(i)
    for i in nums2:
        print(i)
        
# M - length of nums2
# O(N * M)
def example2(nums1, nums2):
    for i in nums1:
        for j in nums2:
            print(i, j)
    
example2(nums1, nums2)